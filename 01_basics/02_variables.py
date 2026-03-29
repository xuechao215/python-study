# 02_variables.py
# 变量和数据类型

# 1. 变量声明
# 在 JS 中: let x = 10;
# 在 Python 中: 不需要关键字，直接赋值
x = 10
y = "Hello"
z = 3.14
is_active = True  # 注意 True 首字母大写 (JS 是 true)

print(f"x: {x}, y: {y}, z: {z}, is_active: {is_active}")

# 2. 动态类型 (Dynamic Typing)
# 类似于 JS，Python 也是动态类型的
x = "Now I am a string"
print(f"x is now: {x}")

# 3. 常见数据类型
# - int (整数)
# - float (浮点数)
# - str (字符串)
# - bool (布尔值)
# - None (空值, 类似于 JS 的 null)

# 4. 类型检查 (type())
# 类似于 JS 的 typeof
print(f"Type of x: {type(x)}")
print(f"Type of y: {type(y)}")
print(f"Type of z: {type(z)}")
print(f"Type of is_active: {type(is_active)}")

# 5. 类型转换 (Type Casting)
# 类似于 JS 的 Number("10"), String(10)
num_str = "100"
num_int = int(num_str)  # 转换为整数
num_float = float(num_str)  # 转换为浮点数
str_val = str(123)  # 转换为字符串

print(f"num_int: {num_int}, type: {type(num_int)}")

# 6. 多变量赋值 (Multiple Assignment)
a, b, c = 1, 2, 3
print(f"a: {a}, b: {b}, c: {c}")

# 交换变量 (Swap) - Python 非常简洁
a, b = b, a
print(f"After swap -> a: {a}, b: {b}")

# 7. 命名规范
# Python 推荐使用 snake_case (蛇形命名法)，而 JS 推荐 camelCase (驼峰命名法)
user_name = "Alice"  # Python 风格
userName = "Bob"     # JS 风格 (虽然在 Python 中也有效，但不推荐)
