import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = 'localhost'
    port = 9999

    # Connection to hostname on the port
    client_socket.connect((host, port))

    print("Connected to server on port", port)

    while True:
        # Send data to the server
        message = input("Enter message to send to server: ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode())

        # Receive data from the server
        response = client_socket.recv(1024)
        if not response:
            break
        print("Received from server:", response.decode())

    client_socket.close()

if __name__ == "__main__":
    start_client()
