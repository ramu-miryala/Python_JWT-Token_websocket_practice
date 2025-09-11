# websocket_client.py
import asyncio
import websockets

async def communicate():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello from client!")
        response = await websocket.recv()
        print(f"Received: {response}")

if __name__ == "__main__":
    asyncio.run(communicate())
