# 01_imports.py
# 模块与导入 (Modules & Imports)
# 类似于 JS 的 import/export (ES Modules) 或 require (CommonJS)

print("=" * 60)
print("1. 导入整个模块")
print("=" * 60)
# import module_name
# 导入整个模块，使用时需要加上模块名前缀
import math

print(f"Pi: {math.pi}")
print(f"Sqrt(16): {math.sqrt(16)}")
print(f"Sin(π/2): {math.sin(math.pi/2)}")

# 优点：避免命名冲突，清晰知道函数/变量来自哪个模块
# 缺点：代码稍长

print("\n" + "=" * 60)
print("2. 导入特定成员")
print("=" * 60)
# from module_name import member_name
# 只导入需要的成员，可以直接使用
from math import pi, sqrt, sin, cos

print(f"Pi (direct): {pi}")
print(f"Sqrt (direct): {sqrt(25)}")
print(f"Sin(π/2) (direct): {sin(pi/2)}")
print(f"Cos(0) (direct): {cos(0)}")

# 优点：代码简洁，不需要模块名前缀
# 缺点：如果导入多个模块有同名成员，会造成命名冲突

print("\n" + "=" * 60)
print("3. 导入所有成员 (不推荐)")
print("=" * 60)
# from module_name import *
# 导入模块中的所有公开成员
# 容易造成命名冲突，不推荐在生产代码中使用

# 示例（注释掉，因为会污染命名空间）：
# from math import *
# print(f"Pi from * import: {pi}")
# print(f"e from * import: {e}")

# 问题示例：
# 假设有两个模块都有名为 'log' 的函数
# from math import *  # math.log 是自然对数
# from custom_module import *  # custom_module.log 是自定义日志函数
# 现在 log() 调用的是哪个？会产生混淆！

print("\n" + "=" * 60)
print("4. 别名 (Alias)")
print("=" * 60)
# as keyword
# 类似于 JS 的 import { member as alias }
import datetime as dt
from math import pow as power
import numpy as np  # 科学计算常用别名
import pandas as pd  # 数据分析常用别名

print(f"Current time: {dt.datetime.now()}")
print(f"2^3: {power(2, 3)}")

# 别名的常见用途：
# 1. 缩短长模块名
# 2. 避免命名冲突
# 3. 遵循社区约定（如 np, pd）

print("\n" + "=" * 60)
print("5. 模块搜索路径 (sys.path)")
print("=" * 60)
import sys

# Python 会按照 sys.path 中的目录顺序查找模块
# 搜索顺序：
# 1. 当前目录（运行脚本的目录）
# 2. PYTHONPATH 环境变量指定的目录
# 3. Python 标准库目录
# 4. site-packages 目录（pip 安装的第三方包）

print("Module search path (前10个):")
for i, path in enumerate(sys.path[:10], 1):
    print(f"{i:2}. {path}")

if len(sys.path) > 10:
    print(f"... 还有 {len(sys.path) - 10} 个路径")

# 动态添加搜索路径
print("\n动态添加搜索路径示例:")
current_path_count = len(sys.path)
custom_path = "/tmp/my_custom_modules"
sys.path.append(custom_path)
print(f"添加了路径: {custom_path}")
print(f"现在 sys.path 有 {len(sys.path)} 个路径")

# 注意：添加的路径只在当前会话有效
# 永久添加路径需要设置 PYTHONPATH 环境变量

print("\n" + "=" * 60)
print("6. __name__ == '__main__' 惯用写法")
print("=" * 60)
# 这是一个非常重要的Python惯用写法
# 作用：区分模块是被直接运行还是被导入

def helper_function():
    """辅助函数，可以被其他模块导入使用"""
    return "I'm a helper function"

def calculate_something():
    """计算函数，可以被其他模块导入使用"""
    return 42

def run_tests():
    """测试函数，只在直接运行时执行"""
    print("Running tests...")
    print(f"Helper: {helper_function()}")
    print(f"Calculation: {calculate_something()}")
    print("Tests completed!")

def main():
    """主函数，包含主要的程序逻辑"""
    print("=" * 40)
    print("程序开始运行")
    print("=" * 40)

    # 调用其他函数
    result = helper_function()
    print(f"Helper function result: {result}")

    value = calculate_something()
    print(f"Calculated value: {value}")

    print("=" * 40)
    print("程序运行结束")
    print("=" * 40)

# 关键部分：检查 __name__
if __name__ == "__main__":
    # 这个代码块只在直接运行此文件时执行
    # 例如：python 01_imports.py
    main()
    print("\n注意：这个文件是直接运行的，__name__ =", __name__)
else:
    # 这个代码块在此文件被导入时执行
    # 例如：import 01_imports
    print("这个文件被作为模块导入了，__name__ =", __name__)
    print("导入了以下函数：helper_function(), calculate_something()")

print("\n" + "=" * 60)
print("7. 相对导入 (在包内部使用)")
print("=" * 60)
# 相对导入用于包内部的模块之间相互导入
# 语法：
# from . import module      # 导入同级模块
# from .module import func  # 导入同级模块的函数
# from .. import parent     # 导入父级模块
# from ..sibling import x   # 导入兄弟包中的模块

# 注意：相对导入只能在包内部使用，不能在脚本中直接使用

print("相对导入示例（需要在包结构中才能运行）:")
print("""
# 假设目录结构：
# my_package/
# ├── __init__.py
# ├── module_a.py
# └── subpackage/
#     ├── __init__.py
#     └── module_b.py

# 在 module_b.py 中：
# from .. import module_a           # 导入父级模块
# from ..module_a import some_func  # 导入父级模块的函数
""")

print("\n" + "=" * 60)
print("8. 导入的最佳实践")
print("=" * 60)
print("1. 优先使用 import module 形式，避免命名冲突")
print("2. 使用 from module import member 时，只导入需要的成员")
print("3. 避免使用 from module import *（星号导入）")
print("4. 使用有意义的别名，特别是长模块名")
print("5. 将导入语句放在文件顶部，按标准库、第三方库、本地模块分组")
print("6. 使用 __name__ == '__main__' 来组织可执行代码")
print("7. 对于包内部的导入，使用相对导入")

print("\n" + "=" * 60)
print("导入语句的标准顺序")
print("=" * 60)
print("""
# 1. 标准库导入
import os
import sys
import math

# 2. 第三方库导入
import numpy as np
import pandas as pd

# 3. 本地应用/库导入
from my_module import my_function
from . import sibling_module  # 相对导入
""")

print("\n" + "=" * 60)
print("总结")
print("=" * 60)
print("Python的模块系统非常灵活，提供了多种导入方式。")
print("理解 sys.path 和 __name__ 是掌握模块导入的关键。")
print("遵循最佳实践可以写出更清晰、更易维护的代码。")
