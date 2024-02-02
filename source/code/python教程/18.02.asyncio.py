#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# [sync_start]
import asyncio
async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
asyncio.run(main())
# [sync_end]

# [compare_start]
import asyncio
import time 

async def count1():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def work1():
    await asyncio.gather(count1(), count1(), count1())

def v1():
    import time
    s = time.perf_counter()
    asyncio.run(work1())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

def v2():
    s = time.perf_counter()
    work2()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

def count2():
    print("One")
    time.sleep(1)
    print("Two")

def work2():
    for _ in range(3):
        count2()

if __name__ == "__main__":
    v1()
    v2()
# [compare_end]




