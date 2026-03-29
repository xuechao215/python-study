# 03_magic_methods.py
# 魔术方法 (Magic Methods) / 双下划线方法 (Dunder Methods)
# 这些方法让 Python 的对象可以像内置类型一样工作

# 1. 字符串表示 (__str__, __repr__)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # __str__ - 面向用户 (print(), str())
    # 类似于 JS 的 toString()
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    # __repr__ - 面向开发者 (repl, debug)
    # 应该返回一个无歧义的字符串表示，最好能用 eval() 重新创建对象
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

# 2. 运算符重载 (Operator Overloading)
# __add__ (+), __sub__ (-), __mul__ (*), __eq__ (==), __lt__ (<), etc.
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

# 3. 长度 (__len__)
# len(obj)
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def __len__(self):
        return len(self.items)
    
    # __getitem__ - 索引访问 (obj[key])
    def __getitem__(self, index):
        return self.items[index]

# 4. 测试
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point(1, 2)

print(f"p1: {p1}")        # Calls __str__
print(f"repr(p1): {repr(p1)}") # Calls __repr__

print(f"p1 + p2 = {p1 + p2}") # Calls __add__
print(f"p1 == p3: {p1 == p3}") # Calls __eq__

cart = ShoppingCart()
cart.add("Apple")
cart.add("Banana")

print(f"Cart size: {len(cart)}") # Calls __len__
print(f"First item: {cart[0]}")  # Calls __getitem__
