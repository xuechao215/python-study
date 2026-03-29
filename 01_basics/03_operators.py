# 03_operators.py
# 运算符

# 1. 算术运算符 (Arithmetic)
a = 10
b = 3
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")  # 除法 (总是返回浮点数，即使整除)
print(f"a // b = {a // b}") # 整除 (Floor Division) - 类似于 JS 的 Math.floor(a/b)
print(f"a % b = {a % b}")  # 取余
print(f"a ** b = {a ** b}") # 幂运算 (JS 中是 a ** b 或 Math.pow(a, b))

# 2. 赋值运算符 (Assignment)
c = 5
c += 2  # c = c + 2
c -= 1
c *= 3
c /= 2
c //= 2
c %= 2
c **= 2
print(f"c = {c}")

# 3. 比较运算符 (Comparison)
# ==, !=, >, <, >=, <=
# 注意: Python 中可以连写比较，JS 中不行
x = 5
print(f"3 < x < 10: {3 < x < 10}")  # True
# JS 等价于: 3 < x && x < 10

# 4. 逻辑运算符 (Logical)
# JS: &&, ||, !
# Python: and, or, not
t = True
f = False
print(f"t and f: {t and f}")
print(f"t or f: {t or f}")
print(f"not t: {not t}")

# 5. 身份运算符 (Identity)
# is, is not
# 检查两个变量是否引用同一个对象 (内存地址相同)
# 类似于 JS 的 === (严格相等)，但用于对象引用
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(f"x is z: {x is z}")  # True
print(f"x is y: {x is y}")  # False (虽然值相同，但对象不同)
print(f"x == y: {x == y}")  # True (值相同)

# 6. 成员运算符 (Membership)
# in, not in
# 检查值是否在序列中 (列表, 元组, 字符串)
my_list = [1, 2, 3, 4, 5]
print(f"3 in my_list: {3 in my_list}")
print(f"6 not in my_list: {6 not in my_list}")
print(f"'H' in 'Hello': {'H' in 'Hello'}")
