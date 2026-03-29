# 01_typing.py
# 类型提示 (Type Hints)
# 类似于 TypeScript

from typing import List, Dict, Optional, Union, Any, Tuple

# 1. 基础类型
# 变量声明
name: str = "Alice"
age: int = 30
is_active: bool = True
height: float = 1.75

# 2. 容器类型 (Generics)
# 类似于 TS: Array<number>, Record<string, number>
scores: List[int] = [10, 20, 30]
user: Dict[str, Any] = {"name": "Bob", "age": 25}
coords: Tuple[int, int] = (10, 20)

# 3. Optional 和 Union
# Optional[T] 等价于 Union[T, None] (类似于 T | null)
# Union[A, B] 等价于 A | B
def get_user(user_id: Optional[int] = None) -> Union[Dict[str, str], None]:
    if user_id:
        return {"name": "Alice"}
    return None

# 4. 类型别名 (Type Aliases)
# 类似于 type UserID = int
UserId = int
def get_by_id(uid: UserId) -> str:
    return f"User {uid}"

# 5. Any
# 类似于 TS 的 any (尽量避免使用)
def process_data(data: Any):
    print(data)

# 6. 自定义类类型
class Person:
    def __init__(self, name: str):
        self.name = name

def greet(p: Person) -> str:
    return f"Hello, {p.name}"

# 7. 静态类型检查工具 (MyPy)
# Python 解释器运行时会忽略这些类型提示
# 需要使用 mypy 等工具进行检查
# pip install mypy
# mypy 01_typing.py
