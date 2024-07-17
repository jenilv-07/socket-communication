import socket

# Define the socket file path
socket_file = '/home/jenilv/code/soketpy/unix_socket'

# Create a Unix socket
client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(socket_file)

# Send data
message = "Hello from client!"
client_socket.sendall(message.encode('utf-8'))

# Receive data
data = client_socket.recv(1024)
print(f"Received: {data.decode('utf-8')}")

# Close the connection
client_socket.close()
