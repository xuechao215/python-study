# SQLAlchemy Session
# 负责数据库连接和会话管理

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 1. 创建 Engine
# check_same_thread=False 仅用于 SQLite
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False} if "sqlite" in settings.SQLALCHEMY_DATABASE_URI else {}
)

# 2. 创建 SessionLocal 类
# 每个请求都会创建一个独立的 Session 实例
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. 依赖项 (Dependency)
# 用于 FastAPI 的依赖注入，确保每个请求使用完数据库后自动关闭连接
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
