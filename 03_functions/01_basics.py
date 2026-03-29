# 01_basics.py
# 函数 (Function)
# 类似于 JS 的 function

# 1. 定义函数
# 使用 def 关键字
def greet(name):
    """
    这是一个文档字符串 (Docstring)
    用于描述函数的功能
    """
    print(f"Hello, {name}!")

# 2. 调用函数
greet("Alice")

# 3. 返回值 (Return Values)
# 如果没有 return，默认返回 None
def add(a, b):
    return a + b

result = add(3, 5)
print(f"Result: {result}")

# 4. 默认参数 (Default Arguments)
# 类似于 JS 的 function(name="World")
def power(base, exponent=2):
    return base ** exponent

print(f"Power (default): {power(3)}")  # 3^2 = 9
print(f"Power (custom): {power(3, 3)}") # 3^3 = 27

# 5. 关键字参数 (Keyword Arguments)
# 调用时指定参数名，顺序无关
print(f"Keyword args: {power(exponent=3, base=2)}")  # 2^3 = 8

# 6. 类型提示 (Type Hints) - Python 3.5+
# 类似于 TypeScript，但只是提示，不会强制检查 (除非使用 MyPy 等工具)
def multiply(a: int, b: int) -> int:
    return a * b

print(f"Multiply: {multiply(4, 5)}")

# 7. 函数作为对象 (First-class Citizens)
# 函数可以作为参数传递，也可以作为返回值
def apply_operation(func, x, y):
    return func(x, y)

print(f"Apply add: {apply_operation(add, 10, 20)}")
