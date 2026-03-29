# ORM 模型 (Database Models)
# 这里定义的是数据库表的结构
# 类似于 Mongoose Schema 或 TypeORM Entity

from sqlalchemy import Boolean, Column, Integer, String, Float
from app.db.base import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    tax = Column(Float, nullable=True)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Item(id={self.id}, title='{self.title}')>"
