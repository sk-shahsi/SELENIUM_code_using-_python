import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))
s.listen(4)
while True:
    clint, addr = s.accept()
    clint.send(bytes("Hey there, what up??", 'utf-8'))
    clint.close()
    print(addr)
    clint.close()
