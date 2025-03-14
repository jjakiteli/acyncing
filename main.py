import asyncio


async def sleep_print(s: str, t: int) -> str:
    await asyncio.sleep(t)
    if s == "error":
        raise ValueError("error")
    
    print(s)
    return s
    
async def main1():
    print("main1--------------------------------")
    try:
        s = await sleep_print("Task 1", 5)
        s = await sleep_print("error", 4)
        s = await sleep_print(f"{s} Task 2", 3)
        await sleep_print(f"{s} Task 3", 1)
    except ValueError as e:
        print(f"main1 encountered an error: {e}")
        
    print("main1 All tasks finished!")
    
async def main2():
    print("main2--------------------------------")
    results = await asyncio.gather(
        sleep_print("Task 1", 5),
        sleep_print("error", 4),
        sleep_print("Task 2", 3),
        sleep_print("Task 3", 1),
        return_exceptions=True
    )
    
    for result in results:
        if isinstance(result, Exception):
            print(f"main2 encountered an error: {result}")
            
    print("main2 All tasks finished!")

async def main3():
    print("main3--------------------------------")
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(sleep_print("Task 1", 2))
            task2 = tg.create_task(sleep_print("error", 2))
            task3 = tg.create_task(sleep_print("Task 2", 3))
            task4 = tg.create_task(sleep_print("Task 3", 1))
    except Exception as e:
        print(f"main3 encountered an error: {e}")

    print("main3 All tasks finished!")
    
    
asyncio.run(main1())
asyncio.run(main2())
asyncio.run(main3())