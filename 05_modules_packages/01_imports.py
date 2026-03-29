# 01_imports.py
# 模块与导入 (Modules & Imports)
# 类似于 JS 的 import/export (ES Modules) 或 require (CommonJS)

# 1. 导入整个模块
# import module_name
import math

print(f"Pi: {math.pi}")
print(f"Sqrt(16): {math.sqrt(16)}")

# 2. 导入特定成员
# from module_name import member_name
from math import pi, sqrt

print(f"Pi (direct): {pi}")
print(f"Sqrt (direct): {sqrt(25)}")

# 3. 导入所有成员 (不推荐)
# from module_name import *
# 容易造成命名冲突
# from math import *

# 4. 别名 (Alias)
# as keyword
# 类似于 JS 的 import { member as alias }
import datetime as dt
from math import pow as power

print(f"Current time: {dt.datetime.now()}")
print(f"2^3: {power(2, 3)}")

# 5. 模块搜索路径 (sys.path)
import sys
# Python 会按照 sys.path 中的目录顺序查找模块
# 通常包含: 当前目录, PYTHONPATH 环境变量, 标准库目录, site-packages (pip 安装的包)
print("Module search path:")
for path in sys.path:
    print(path)

# 6. __name__ == "__main__"
# 这是一个非常有用的惯用写法
# 当模块被直接运行时，__name__ 的值为 "__main__"
# 当模块被导入时，__name__ 的值为模块名
# 类似于 JS 的 if (require.main === module)

def main():
    print("This script is running directly.")

if __name__ == "__main__":
    main()
else:
    print("This script is imported as a module.")
