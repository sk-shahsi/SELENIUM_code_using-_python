from tkinter import *


root = Tk()
entry = Entry()
entry.pack(side=BOTTOM)
listvox = Listbox()
listvox.pack()
button = Button(root, text="Send")
button.pack(side=BOTTOM)

root.mainloop()
