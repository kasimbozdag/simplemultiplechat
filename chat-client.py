import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the hostname of the server computer (Mac 1)
host = '192.168.68.109'  # Replace with the correct IP address
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Function to send messages
def send_message():

    while True:
        message = input()
        client_socket.send(message.encode())

# Function to receive messages
def receive_messages():
    while True:
        message = client_socket.recv(1024).decode()
        print(f"{message}")

# Start separate threads for sending and receiving messages
import threading
send_thread = threading.Thread(target=send_message)
recv_thread = threading.Thread(target=receive_messages)

send_thread.start()
recv_thread.start()
