import asyncio


async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)  # Simulate a delay
    print("Task 1 finished")


async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)  # Simulate a shorter delay
    print("Task 2 finished")


async def main():
    # Schedule both tasks to run concurrently
    await asyncio.gather(task1(), task2())


# Get the event loop and run the main function until completion
asyncio.run(main())
