# 02_standard_library.py
# 标准库概览 (Standard Library Overview)
# Python 自带了很多强大的模块 (Battery Included)

import os
import sys
import math
import random
import datetime
import json
import re

# 1. os - 操作系统接口
print(f"Current working directory: {os.getcwd()}")
# os.mkdir("test_dir") # 创建目录
# os.rmdir("test_dir") # 删除目录
print(f"Path separator: {os.path.sep}")

# 2. sys - 系统相关
print(f"Python version: {sys.version}")
# sys.argv - 命令行参数 (类似于 JS 的 process.argv)
print(f"Command line args: {sys.argv}")
# sys.exit(0) - 退出程序

# 3. math - 数学函数
print(f"Pi: {math.pi}")
print(f"Sin(Pi/2): {math.sin(math.pi/2)}")
print(f"Ceil(3.14): {math.ceil(3.14)}")

# 4. random - 随机数生成
print(f"Random float (0-1): {random.random()}")
print(f"Random int (1-10): {random.randint(1, 10)}")
print(f"Choice from list: {random.choice(['a', 'b', 'c'])}")

# 5. datetime - 日期和时间
now = datetime.datetime.now()
print(f"Current time: {now}")
print(f"Formatted time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 6. json - JSON 处理
data = {"name": "Alice", "age": 30, "city": "New York"}
json_str = json.dumps(data)
print(f"JSON String: {json_str}")
parsed_data = json.loads(json_str)
print(f"Parsed Dict: {parsed_data}")

# 7. re - 正则表达式
text = "The rain in Spain"
# re.search() - 查找第一个匹配
match = re.search(r"^The.*Spain$", text)
if match:
    print("YES! We have a match!")
else:
    print("No match")

# re.findall() - 查找所有匹配
print(f"Find all 'ai': {re.findall('ai', text)}")

# re.sub() - 替换
print(f"Replace 'Spain' with 'France': {re.sub('Spain', 'France', text)}")
