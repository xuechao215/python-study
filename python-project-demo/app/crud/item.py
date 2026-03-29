# CRUD 模块 (Create, Read, Update, Delete)
# 将数据库操作逻辑从 Router 中分离出来，便于测试和复用
# 类似于 Service Layer 或 DAO Layer

from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate
from typing import List, Optional

def get_item(db: Session, item_id: int) -> Optional[Item]:
    return db.query(Item).filter(Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    return db.query(Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: ItemCreate) -> Item:
    db_item = Item(
        title=item.title,
        description=item.description,
        price=item.price,
        tax=item.tax,
        is_active=True
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, db_item: Item, item_update: ItemUpdate) -> Item:
    # 动态更新属性
    update_data = item_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, db_item: Item) -> Item:
    db.delete(db_item)
    db.commit()
    return db_item
