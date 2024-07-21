import asyncio


async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print(f"Received {message} from {addr}")

    writer.write("Hello from server".encode())
    await writer.drain()

    print("Closing the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 12345)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()


asyncio.run(main())
