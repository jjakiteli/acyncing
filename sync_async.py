import time
import asyncio
import concurrent.futures

def sync_function(s: str, t: int):
    print(f"Running sync {s} function")
    time.sleep(t)
    print(f"Finished sync {s} function")
    return f"Sync {s} Result"

async def async_function(s: str, t: int):
    print(f"Running async {s} function")
    await asyncio.sleep(t)
    print(f"Finished async {s} function")
    return f"Async {s} Result"

async def main():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result_sync1, result_sync2, result_async1, result_async2 = await asyncio.gather(
            loop.run_in_executor(pool, sync_function, "1", 3),
            loop.run_in_executor(pool, sync_function, "2", 1),
            async_function("1", 3),
            async_function("2", 1),
        )
    print(result_sync1, result_sync2, result_async1, result_async2)

asyncio.run(main())