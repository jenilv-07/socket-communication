import socket
import os

# Define the socket file path
socket_file = '/home/jenilv/code/soketpy/unix_socket'

# Ensure the socket file does not already exist and is not a directory
if os.path.exists(socket_file):
    if os.path.isdir(socket_file):
        raise OSError(f"Socket file path is a directory: {socket_file}")
    else:
        os.remove(socket_file)

try:
    # Create a Unix socket
    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # Bind the socket to the file path
    server_socket.bind(socket_file)

    # Listen for incoming connections
    server_socket.listen(1)

    print(f"Server listening on {socket_file}")

    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print("Accepted connection")

        # Receive data
        data = client_socket.recv(1024)
        if data:
            print(f"Received: {data.decode('utf-8')}")
            client_socket.sendall(b"Hello from server!")

        # Close the connection
        client_socket.close()
finally:
    # Clean up the socket file
    if os.path.exists(socket_file):
        os.remove(socket_file)
