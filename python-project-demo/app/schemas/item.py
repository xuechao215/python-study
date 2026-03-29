# Pydantic Schemas (Data Transfer Objects - DTOs)
# 这里定义的是 API 请求和响应的数据结构 (JSON Schema)
# 与 app/models (ORM) 分离，类似于 Interface vs Entity

from pydantic import BaseModel, Field
from typing import Optional

# 1. 基础模型 (Base Model)
# 包含所有公共字段
class ItemBase(BaseModel):
    title: str = Field(..., title="The title of the item", max_length=100)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    tax: Optional[float] = None

# 2. 创建模型 (Create Model) - 用于 POST 请求体
class ItemCreate(ItemBase):
    pass

# 3. 更新模型 (Update Model) - 用于 PUT/PATCH 请求体
class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: Optional[float] = None
    is_active: Optional[bool] = None

# 4. 响应模型 (Response Model) - 用于 API 响应
# 包含数据库生成的字段 (如 id)
class Item(ItemBase):
    id: int
    is_active: bool

    # ConfigDict 用于配置模型行为 (Pydantic V2)
    # from_attributes=True 允许从 ORM 对象读取数据 (ORM mode)
    class Config:
        from_attributes = True
