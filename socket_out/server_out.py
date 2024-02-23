import socket

def server():
    host = socket.gethostname()
    port = 21042
    s = socket.socket()
    s.bind((host, port))
    s.listen(2)
    c, address_ = s.accept()
    print(f"Connected to: {address}")
    while True:
        data = c.recv(1024)
        print(f"Received from client: ",data)
        response = input("Enter response to send to client: ")
        c.send(response.encode())
    c.close()


if __name__ == "__main__":
    server()
