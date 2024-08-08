

# Socket Communication Example

This repository contains examples of socket communication between a Python server and both Python and C clients. The Python server listens for incoming connections and communicates with the clients by receiving and sending messages.

## Python Server

The Python server listens for incoming connections on `localhost` at port `9999` and communicates with connected clients.

### How to Run the Python Server

1. Ensure you have Python installed on your machine.
2. Save the Python server code to a file named `server.py`.
3. Open a terminal and navigate to the directory containing `server.py`.
4. Run the server with the following command:
   ```bash
   python server.py
   ```

## Python Client

The Python client connects to the Python server and sends messages to it. It also receives responses from the server.

### How to Run the Python Client

1. Save the Python client code to a file named `client.py`.
2. Open a terminal and navigate to the directory containing `client.py`.
3. Run the client with the following command:
   ```bash
   python client.py
   ```

## C Client

The C client connects to the Python server using socket communication. The client sends messages to the server and receives responses.

### How to Compile and Run the C Client

1. Save the C client code to a file named `client.c`.
2. Open a terminal and navigate to the directory containing `client.c`.
3. Compile the client using `gcc`:
   ```bash
   gcc -o client client.c
   ```
4. Run the compiled client with the following command:
   ```bash
   ./client
   ```

