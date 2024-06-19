import socket
import threading
import sys

def receive_messages(client_socket):
    """Receive messages from the server and print them."""
    while True:
        try:
            # Receive message from the server
            message = client_socket.recv(1024).decode('utf-8').strip()
            if not message:
                break
            # Print server's message
            print(f"Server: {message}")
        except:
            # Close the client socket if an error occurs
            client_socket.close()
            break

def main():
    # Create a TCP/IP socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server running on localhost (127.0.0.1) at port 5555
    client_socket.connect(('127.0.0.1', 5555))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Main loop to send messages from the client
    while True:
        # Get input message from the client console
        message = input("\nClient: ")
        
        # Check if the client wants to exit
        if message.lower() == 'exit':
            print("You left the chat.")
            client_socket.close()  # Close the client socket
            sys.exit()  # Exit the program
            
        # Send the message to the server
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
