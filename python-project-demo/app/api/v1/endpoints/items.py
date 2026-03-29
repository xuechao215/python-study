# Router (Controller)
# 类似于 Express 的 Router，负责 HTTP 请求的处理
# 调用 CRUD 层进行业务逻辑处理

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.item import Item, ItemCreate, ItemUpdate
from app.crud.item import get_item, get_items, create_item, update_item, delete_item
from app.db.session import get_db

router = APIRouter()

# GET /items
@router.get("/", response_model=List[Item])
async def read_items(
    skip: int = 0,
    limit: int = 100,
    # 依赖注入 (Dependency Injection) - 获取数据库会话
    db: Session = Depends(get_db)
):
    """
    Get all items with pagination.
    """
    items = get_items(db, skip=skip, limit=limit)
    return items

# GET /items/{item_id}
@router.get("/{item_id}", response_model=Item)
async def read_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    """
    Get an item by ID.
    """
    db_item = get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# POST /items
@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_new_item(
    item: ItemCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new item.
    """
    return create_item(db=db, item=item)

# PUT /items/{item_id}
@router.put("/{item_id}", response_model=Item)
async def update_existing_item(
    item_id: int,
    item_update: ItemUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing item.
    """
    db_item = get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return update_item(db=db, db_item=db_item, item_update=item_update)

# DELETE /items/{item_id}
@router.delete("/{item_id}", response_model=Item)
async def delete_existing_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an item.
    """
    db_item = get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return delete_item(db=db, db_item=db_item)
