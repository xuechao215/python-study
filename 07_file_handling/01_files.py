# 01_files.py
# 文件处理 (File Handling)
# 类似于 Node.js 的 fs 模块

# 1. 写入文件
# 使用 'w' 模式 (write)，如果文件不存在则创建，如果存在则覆盖
# 使用 with 语句可以自动关闭文件 (推荐做法)
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, Python Files!\n")
    f.write("This is a second line.\n")
    f.write("Python makes file handling easy.\n")

print("File 'example.txt' written successfully.")

# 2. 读取文件
# 使用 'r' 模式 (read)，默认模式
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("\n--- File Content ---")
    print(content)
    print("--------------------")

# 3. 按行读取
with open('example.txt', 'r', encoding='utf-8') as f:
    print("\n--- Reading line by line ---")
    for line in f:
        print(f"Line: {line.strip()}")  # strip() 去除每行末尾的换行符

# 4. 追加内容
# 使用 'a' 模式 (append)
with open('example.txt', 'a', encoding='utf-8') as f:
    f.write("This is an appended line.\n")

# 5. 读取所有行到列表
with open('example.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"\nTotal lines: {len(lines)}")
    print(f"Last line: {lines[-1].strip()}")

# 6. 删除文件
import os
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("\nFile 'example.txt' deleted.")
else:
    print("\nFile does not exist.")
