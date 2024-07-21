import asyncio


async def read_file(file_path):
    with open(file_path, "r") as file:
        content = await asyncio.to_thread(file.read)
        return content


async def main():
    content = await read_file("example.txt")
    print(content)


asyncio.run(main())
