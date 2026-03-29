# SQLAlchemy Base
# 所有 ORM 模型都继承自这个 Base 类

from typing import Any
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass
