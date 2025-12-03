import socket
import threading
from tkinter import *


def send_message():
    message = entry.get()
    if message.strip():
        listbox.insert(END, "Server: " + message)
        client.send(message.encode())
    entry.delete(0, END)


def receive_message():
    while True:
        try:
            msg = client.recv(1024).decode()
            listbox.insert(END, "Client: " + msg)
        except:
            break


def start_server():
    global client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = '127.0.0.1'
    PORT = 5000
    s.bind((HOST, PORT))
    s.listen(1)
    print("Server started... Waiting for client...")

    client, addr = s.accept()
    print("Client connected:", addr)

    threading.Thread(target=receive_message, daemon=True).start()


root = Tk()
root.title("Server Chat")

listbox = Listbox(root, width=50, height=15)
listbox.pack()

entry = Entry(root, width=40)
entry.pack(side=LEFT, padx=5, pady=5)

send_btn = Button(root, text="Send", command=send_message)
send_btn.pack(side=LEFT)

# Start server in background thread
threading.Thread(target=start_server, daemon=True).start()

root.mainloop()
