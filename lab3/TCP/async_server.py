import asyncio
from typing import List

SERVER_HOST = ""
SERVER_PORT = 5005

wiersz: List[str] = []

barier = asyncio.Barrier(3)


async def handle_client(reader, writer):
    while True:
        data = await reader.read(1024)
        wiersz.append(data.decode("utf-8"))
        if not data:
            break
    writer.close()
    await barier.wait()
    server.close()
    await server.wait_closed()


async def main():
    global server
    server = await asyncio.start_server(handle_client, SERVER_HOST, SERVER_PORT)

    async with server:
        await server.serve_forever()


try:
    asyncio.run(main())
except asyncio.CancelledError:

    wiersz = [x for x in "".join(wiersz).split("|") if x != ""]
    wiersz = list(
        map(lambda x: x.replace("(", "").replace(")", "").strip().split(","), wiersz)
    )
    wiersz = map(lambda x: (int(x[0]), x[1].strip().replace("'", "")), wiersz)
    wiersz = sorted(wiersz, key=lambda x: x[0])
    print(" ".join(map(lambda x: x[1], wiersz)))
