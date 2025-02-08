import asyncio
import websockets
import json

connected_clients = set()


async def register(websocket):
    connected_clients.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        connected_clients.remove(websocket)


async def handle_message(websocket, message):
    data = json.loads(message)
    # 处理接收到的消息
    response = {"message": "Message received", "data": data}
    await websocket.send(json.dumps(response))


async def server(websocket, path):
    await register(websocket)
    async for message in websocket:
        await handle_message(websocket, message)


async def start_websocket_server():
    async with websockets.serve(server, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(start_websocket_server())
