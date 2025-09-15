import asyncio
import websockets

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    print(f"[Server] New client connected at path: {path}")
    try:
        async for message in websocket:
            print(f"[Server] Received from client: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.ConnectionClosedOK:
        print(f"[Server] Client disconnected gracefully.")
    except Exception as e:
        print(f"[Server] Exception: {e}")
    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server running at ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
