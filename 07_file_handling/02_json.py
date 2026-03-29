# 02_json.py
# JSON 处理 (JSON Handling)
# Python 自带 json 模块，非常方便

import json

# 1. 字典转 JSON (Serialization / Encoding)
# 类似于 JSON.stringify()
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "JavaScript", "HTML"],
    "is_active": True,
    "address": {
        "city": "New York",
        "zip": "10001"
    },
    "projects": None
}

# json.dumps() - 返回字符串
json_str = json.dumps(data, indent=4)  # indent=4 格式化输出
print(f"JSON String:\n{json_str}")

# 2. 写入 JSON 文件
# json.dump() - 写入文件对象
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
print("\nJSON file 'data.json' created.")

# 3. JSON 转字典 (Deserialization / Decoding)
# 类似于 JSON.parse()
json_input = '{"name": "Bob", "age": 25, "is_active": false}'
parsed_data = json.loads(json_input)
print(f"\nParsed from String: {parsed_data}")
print(f"Name: {parsed_data['name']}")
print(f"Is Active: {parsed_data['is_active']}")  # 注意 false 变成了 False

# 4. 读取 JSON 文件
# json.load() - 从文件对象读取
try:
    with open("data.json", "r") as f:
        file_data = json.load(f)
        print(f"\nRead from File: {file_data}")
        print(f"First Skill: {file_data['skills'][0]}")
except FileNotFoundError:
    print("\nFile not found.")

# 5. 清理文件
import os
if os.path.exists("data.json"):
    os.remove("data.json")
    print("\nFile 'data.json' deleted.")
