import socket
from tkinter import *

def send(listbox,entry):
    message = entry.get()
    listbox.insert('end',"Server: "+message)
    entry.delete(0,END)
    clint.send(bytes(message, 'utf-8'))

def recive(listbox):
    message_from_clint = clint.recv(50)
    listbox.insert('end',"Clint: "+message_from_clint.decode('utf-8'))
root = Tk()
entry = Entry()
entry.pack(side=BOTTOM)
listbox = Listbox()
listbox.pack()
button = Button(root, text="Send",command = lambda:send(listbox,entry))
button.pack(side=BOTTOM)

rbutton = Button(root, text="Resieve",command = lambda:recive(listbox))
rbutton.pack(side=BOTTOM)

root.title("Server:")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))
s.listen(4)
clint, addr = s.accept()




root.mainloop()
