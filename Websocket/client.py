import asyncio
import websockets

async def chat():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to server.")

        while True:
            message = input("You: ")
            await websocket.send(message)

            try:
                response = await websocket.recv()
                print(f"[Server]: {response}")
            except websockets.exceptions.ConnectionClosedOK:
                print("Server closed connection.")
                break
            except websockets.exceptions.ConnectionClosedError as e:
                print(f"Connection closed with error: {e}")
                break

if __name__ == "__main__":
    asyncio.run(chat())
