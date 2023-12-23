"""
This module depicts how to write simple Async IO code
"""

import time
import asyncio


async def access_db():
    print("accessing database")
    await asyncio.sleep(2) #event loop looks for other tasks in queue while this task is busy
    #event loop continues from here and finishes access_db
    print("finished accessing database")


async def access_files():
    print("accessing files")
    await asyncio.sleep(2) #event loop looks for other tasks in queue while this task is busy
    #event loop continues from here and finishes access_files
    print("finished accessing files")


async def main():
    print("starting")
    start = time.time()

    # await access_db() #run one coroutine, wait for it to finish
    # await access_files() #run another coroutine wait for it to finish

    await asyncio.gather(access_db(), access_files()) #start both coroutines at the same time and wait for them to finish
    #event loop returns from main's waiting and continues executing code here
    duration = time.time() - start
    print(f"{duration: 0.2f} seconds")

if __name__ == '__main__':
    asyncio.run(main()) #begin asyncio event loop, can't start another event loop inside main