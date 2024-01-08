import socket

def start_server():
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set ip/domain and port
    server_address = ('0.0.0.0', 4446)

    # Bind ip and port to socket
    server_socket.bind(server_address)

    # Set socket for listening
    server_socket.listen(1)
    print(f"Listening on {server_address}")

    while True:
        # Wait for connection
        print("Waiting for connection...")
        client_socket, client_address = server_socket.accept()
        print(f"Client connected: {client_address}")

        try:
            # Get numbers from client
            data = client_socket.recv(1024).decode('utf-8')

            # Split it into numbers
            numbers = [int(num) for num in data.split()]

            # Sum these numbers
            result = sum(numbers)

            # Respond result
            client_socket.sendall(str(result).encode('utf-8'))

        finally:
            # Close connection
            client_socket.close()

if __name__ == "__main__":
    start_server()
