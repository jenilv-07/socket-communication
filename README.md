# Socket Communication Example

This repository contains examples of socket communication between a Python server and a C client. The Python server listens for incoming connections and communicates with the C client by receiving and sending messages.

## Python Server

The Python server listens for incoming connections on `localhost` at port `9999` and communicates with connected clients.

### How to Run the Python Server

1. Ensure you have Python installed on your machine.
2. Save the Python server code to a file named `server.py`.
3. Open a terminal and navigate to the directory containing `server.py`.
4. Run the server with the following command:
   ```bash
   python server.py


# C Client for Socket Communication

This repository contains a C client that connects to a Python server using socket communication. The client sends messages to the server and receives responses.

## How to Compile and Run the C Client

1. Save the C client code to a file named `client.c`.
2. Open a terminal and navigate to the directory containing `client.c`.
3. Compile the client using `gcc`:
   ```bash
   gcc -o client client.c
