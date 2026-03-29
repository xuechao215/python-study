# 01_async_await.py
# 异步编程 (Async/Await)
# 类似于 JS 的 async/await

import asyncio
import time

# 1. 定义异步函数 (Coroutine)
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

# 2. 运行异步函数
async def main():
    print(f"started at {time.strftime('%X')}")

    # 串行执行 (Sequential)
    # 类似于 JS: await say_after(1, 'hello'); await say_after(2, 'world');
    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

# 3. 启动事件循环 (Event Loop)
# Python 3.7+ 使用 asyncio.run()
# JS 中事件循环是自动启动的
if __name__ == "__main__":
    asyncio.run(main())
