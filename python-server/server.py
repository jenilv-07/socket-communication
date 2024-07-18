import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = 'localhost'
    port = 9999

    # Bind the socket to the port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)

    print("Server listening on port", port)

    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print("Got a connection from", addr)

        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break
            print("Received from client:", data.decode())

            # Send data back to the client
            response = input("Enter response to client: ")
            client_socket.send(response.encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()