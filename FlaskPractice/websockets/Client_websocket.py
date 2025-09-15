import asyncio
import websockets

async def communicate():
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            count = 0
            while True:
                message = f"Hello from client #{count}"
                await websocket.send(message)
                print(f"[Client] Sent: {message}")

                response = await websocket.recv()
                print(f"[Client] Received: {response}")

                count += 1
                await asyncio.sleep(3)  # Wait 3 seconds
    except Exception as e:
        print(f"[Client] Exception: {e}")

if __name__ == "__main__":
    asyncio.run(communicate())
