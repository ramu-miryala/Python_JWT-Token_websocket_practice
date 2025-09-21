## How it Works
 Server (s_socket)

Creates a socket:

s_socket = socket.socket()


Binds it to localhost:1000 and listens for 1 connection:

s_socket.bind(('localhost', 1000))
s_socket.listen(1)


Accepts a client connection:

conn, addr = s_socket.accept()


Enters a loop:

Receives client’s message (conn.recv(1024))

Prints it

Reads server’s reply from input() and sends back (conn.send())

# Client (c_socket)

Creates a socket:

c_socket = socket.socket()


Connects to localhost:1000:

c_socket.connect(('localhost', 1000))


Enters a loop:

Reads client’s message from input()

Sends it to server (c_socket.send())

Waits for server reply (c_socket.recv()) and prints it

## How to Run

Save server code in server.py

Save client code in client.py

Run in two terminals:

python server.py


Then in another terminal:

python client.py


Start chatting 

# Limitations

Only one client can connect (because listen(1)).

It’s blocking (server waits for input before responding).

No handling of disconnects/crashes.

# Next Steps (if you want to improve)

Allow multiple clients using threading or asyncio.

Add exit command (if msg.lower() == "exit": break).

Implement a simple chatroom with multiple participants.

Add a GUI (using Tkinter or PyQt) for a chat app feel.