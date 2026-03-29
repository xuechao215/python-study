# 03_context_managers.py
# 上下文管理器 (Context Managers)
# 类似于 JS 的 try/finally 块

# 1. 为什么使用上下文管理器?
# 确保资源在使用后被释放 (如关闭文件，释放锁)
# 避免内存泄漏

# 2. 传统方式 (try/finally)
file = None
try:
    file = open("example.txt", "w")
    file.write("Hello")
finally:
    if file:
        file.close()

# 3. with 语句 (推荐)
# 自动调用 __enter__ 和 __exit__ 方法
with open("example.txt", "w") as file:
    file.write("Hello from context manager!")

# 4. 自定义上下文管理器
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        if exc_type:
            print(f"Exception occurred: {exc_value}")
        return False  # 如果返回 True，则异常会被吞噬

# 使用自定义上下文管理器
with MyContextManager() as cm:
    print("Inside context")
    # raise Exception("Oops!") # 异常会被捕获并处理

# 5. contextlib 模块
# 使用 @contextmanager 装饰器简化自定义上下文管理器的创建
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering (decorator)")
    yield "Resource"
    print("Exiting (decorator)")

with my_context_manager() as resource:
    print(f"Inside: {resource}")

# 6. 删除文件
import os
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("\nFile 'example.txt' deleted.")
