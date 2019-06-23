from tkinter import *


root = Tk()
frameT = Frame(root)
frameM = Frame(root)
frameB = Frame(root)


frameT.config(width=500,height=100,bg="blue")
frameT.pack(side=TOP)

frameM.config(width=500,height=100,bg="red")
frameM.pack()

frameB.config(width=500,height=100,bg="green")
frameB.pack(side=BOTTOM)


root.mainloop()
