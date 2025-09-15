import asyncio
import websockets

clients = set()

async def handle_client(websocket):  # ONLY websocket argument
    print("New client connected")
    clients.add(websocket)
    try:
        async for message in websocket:
            print(f"[Client sent]: {message}")

            # Send back a proper string
            response = f"Server received: {message}"
            await websocket.send(response)

    except websockets.exceptions.ConnectionClosedOK:
        print("Client disconnected normally.")

    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed with error: {e}")

    except Exception as e:
        print(f"Unexpected server error: {repr(e)}")

    finally:
        clients.remove(websocket)
        print("Client removed.")

async def main():
    server = await websockets.serve(handle_client, "localhost", 8765)
    print("Server is running at ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
