# Simple Chat Program (Python)

This is a basic chat program implemented in Python, allowing multiple computers on the same local network to exchange text messages. The program consists of two scripts: `chat-server.py` (to run on the server computer) and `chat-client.py` (to run on client computers).

## Instructions

### Prerequisites

- Python installed on all computers (Python 3.x recommended).
- All computers must be on the same local network.

### Server Setup (Mac 1)

1. Open the `chat-server.py` script on the first computer (Mac 1).

2. Modify the `host` variable in the script to specify the IP address of Mac 1 or use `'localhost'` to bind to the local machine.

3. Set the `port` to a specific port number (e.g., 12345).

4. Run the `chat-server.py` script. It will wait for incoming connections.

### Client Setup (Mac 2, Mac 3, etc.)

1. Open the `chat-client.py` script on the second computer (Mac 2) or any additional client computers.

2. Modify the `host` variable in the script to specify the IP address of the server computer (Mac 1) where `chat-server.py` is running.

3. Set the `port` to the same port number used in the server script (e.g., 12345).

4. Run the `chat-client.py` script. It will connect to the server (Mac 1).

5. When prompted, enter your desired username to join the chat room.

6. Start typing messages to send to other clients.

### Chatting

- Clients can exchange text messages in real-time.
- When a new client joins and provides a username, a "has joined the chat" message is sent to all other clients.
- The server automatically adds the username to the messages sent by clients.
- To exit the chat, you can press `Ctrl+C` in the terminal where the scripts are running to stop the server and client scripts.

## Notes

- This is a simple example for educational purposes and can serve as a starting point for chat application development.
- Customize and enhance the chat program further based on your specific requirements.
