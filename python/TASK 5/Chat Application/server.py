import socket
import threading

def handle_client(client_socket):
    """Handle communication with the client."""
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode('utf-8').strip()
            if not message:
                break
            # Print client's message
            print(f"Client: {message}")
        except:
            # Handle client leaving the chat
            print("Client left the chat.")
            client_socket.close()
            break

def main():
    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow reuse of the address
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the address and port
    server.bind(('0.0.0.0', 5555))
    
    # Listen for incoming connections
    server.listen()
    
    print("Server started and listening on port 5555")

    # Accept a new connection
    client_socket, client_address = server.accept()
    print(f"New connection from {client_address}")

    # Start a new thread to handle communication with the client
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()

    # Main loop to send messages from the server
    while True:
        # Get input message from the server console
        message = input("\nServer: ")
        
        # Send the message to the client
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
