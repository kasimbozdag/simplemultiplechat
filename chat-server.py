import socket
import threading

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the hostname of the current computer
host = '192.168.68.109'  # Replace with the correct IP address
port = 12345

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print("Server is listening for incoming connections...")

# Dictionary to map client sockets to their usernames
client_usernames = {}

# Function to broadcast messages to all clients
def broadcast_message(message, sender_socket=None):
    for client_socket in clients:
        if client_socket != sender_socket:
            client_socket.send(message.encode())

# Function to handle each client
def handle_client(client_socket):

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            # Check if this is the first message from the client (i.e., their username)
            if client_socket not in client_usernames:
                username = message
                client_usernames[client_socket] = username
                welcome_message = f"{username} has joined the chat!"
                print(welcome_message)
                broadcast_message(welcome_message, client_socket)
                client_socket.send("Welcome to the chat room!".encode())
            else:
                # Regular chat message
                sender = client_usernames[client_socket]
                formatted_message = f"{sender}: {message}"
                broadcast_message(formatted_message, client_socket)

        except Exception as e:
            print(f"Error: {e}")
            break

    # Remove the client from the list of clients and close the socket
    if client_socket in client_usernames:
        del client_usernames[client_socket]
    clients.remove(client_socket)
    client_socket.close()

# List to store client connections
clients = []

# Accept and handle incoming connections
while True:
    client, addr = server_socket.accept()
    print(f"Connected by {addr}")

    client.send("Enter your username: ".encode())

    # Add the client to the list of clients
    clients.append(client)

    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

