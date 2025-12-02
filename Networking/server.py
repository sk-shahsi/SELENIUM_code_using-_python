import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostbyname(socket.gethostname())

port = 8083
s.bind((HOST_NAME, port))

s.listen(4)

while True:
    client, addr = s.accept()
    print("Client connected:", addr)

    msg = client.recv(1024).decode()
    print("Client says:", msg)

    client.send("Hello from Server".encode())

    client.close()
