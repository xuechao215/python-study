from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.db.session import get_db, Base

# 1. 使用内存数据库进行测试 (SQLite :memory:)
# StaticPool 确保多线程测试时使用同一个连接
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. 覆盖依赖 (Dependency Override)
# 使用测试数据库替代生产数据库
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# 3. 创建测试客户端
client = TestClient(app)

# 4. 初始化数据库表
Base.metadata.create_all(bind=engine)

def test_create_item():
    response = client.post(
        "/api/v1/items/",
        json={"title": "Test Item", "description": "A test item", "price": 10.5},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Item"
    assert "id" in data
    assert data["is_active"] is True

def test_read_items():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_read_item():
    # 先创建一个 item
    response = client.post(
        "/api/v1/items/",
        json={"title": "Test Item 2", "price": 20.0},
    )
    item_id = response.json()["id"]

    # 获取该 item
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Item 2"
    assert data["id"] == item_id

def test_update_item():
    # 先创建一个 item
    response = client.post(
        "/api/v1/items/",
        json={"title": "To Update", "price": 5.0},
    )
    item_id = response.json()["id"]

    # 更新该 item
    response = client.put(
        f"/api/v1/items/{item_id}",
        json={"title": "Updated Title", "price": 15.0, "is_active": False},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["price"] == 15.0
    assert data["is_active"] is False

def test_delete_item():
    # 先创建一个 item
    response = client.post(
        "/api/v1/items/",
        json={"title": "To Delete", "price": 5.0},
    )
    item_id = response.json()["id"]

    # 删除该 item
    response = client.delete(f"/api/v1/items/{item_id}")
    assert response.status_code == 200

    # 再次获取应该返回 404
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 404
