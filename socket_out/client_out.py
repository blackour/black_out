import socket
def client():
    host = socket.gethostname
    port = 21042
    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input("Enter your message: ")
    while message.lower() != "":
        client_socket.send(message)
        data = client_socket.recv(1024).decode()
        print("Received from server: " + data)
        message = input("Enter your message: ")
    client_socket.close()
if __name__ == "__main__":
    client()
