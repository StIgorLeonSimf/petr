import asyncio
import time


async def f1(n):
    print(n ** 2)
    await asyncio.sleep(3)
    print('F1 complited')


async def f2(n):
    print(n * 5)
    await asyncio.sleep(2)
    print('F2 complited')


async def main():
    # task1 = asyncio.create_task(f1(5))
    # task2 = asyncio.create_task(f2(100))
    # await task1
    # task2
    await asyncio.gather(f1(10), f2(100))

start = time.perf_counter()
asyncio.run(main())
stop = time.perf_counter()
print(round(stop - start, 2))
