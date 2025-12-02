import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Host_Name = socket.gethostbyname(socket.gethostname())
port = 8083

s.connect((Host_Name, port))
s.send("Hello Server".encode())

response = s.recv(1024).decode()
print("Server Response:", response)

s.close()