# 01_hello_world.py
# Python 的 Hello World

# 1. 输出 (Output)
# 在 JavaScript 中我们用 console.log("Hello World")
# 在 Python 中我们用 print("Hello World")

print("Hello, Python World!")

# 2. 注释 (Comments)
# 单行注释使用 # (JS 使用 //)
"""
多行注释可以使用三个双引号 (JS 使用 /* ... */)
但这实际上是一个字符串字面量，如果没有赋值给变量，Python 会忽略它。
"""

# 3. 简单的数学运算
print("5 + 3 =", 5 + 3)

# 4. 字符串格式化 (f-string) - 类似于 JS 的模板字符串 `Hello ${name}`
name = "Frontend Dev"
print(f"Hello, {name}!")  # 注意前面的 'f'
