#  Simple WebSocket Chat Application

##  Overview  
This project demonstrates a simple WebSocket-based chat application using Python’s `websockets` and `asyncio` modules.  
It allows multiple clients to connect to the server and exchange real-time messages in a bidirectional manner.

---

##  Features
- Persistent WebSocket connection between client and server
- Real-time, bidirectional communication
- Simple message exchange between client and server
- Handles connection exceptions gracefully

---

##  How It Works

1. The server listens for WebSocket connections on a specified port.
2. The client connects to the server using the WebSocket URI.
3. Both client and server can send and receive custom messages continuously.
4. The connection remains active until either side closes it.

---

##  Example Flow

- Client connects to the server
- Client sends: `Hello Server!`
- Server responds: `Server received: Hello Server!`
- Server can also send custom messages anytime.

---

##  How to Run

###  Start the WebSocket Server
```bash
python server.py
