# 02_gather.py
# 并发执行 (Concurrency)
# 类似于 JS 的 Promise.all()

import asyncio
import time

async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished")
    return f"Result {name}"

async def main():
    print(f"started at {time.strftime('%X')}")

    # 使用 asyncio.gather() 并发运行多个协程
    # 类似于 JS: const results = await Promise.all([task('A', 2), task('B', 1)])
    results = await asyncio.gather(
        task('A', 2),
        task('B', 1),
        task('C', 3)
    )

    print(f"finished at {time.strftime('%X')}")
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())
