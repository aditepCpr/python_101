from tkinter import *

root = Tk()

frameT = Frame(root)
frameM = Frame(root)
frameB = Frame(root)

frameT.config(width=500,height=100,bg="blue")
frameT.pack(side=TOP)
frameM.config(width=500,height=100,bg="red")
frameM.pack(side=LEFT)
frameB.config(width=500,height=100,bg="green")
frameB.pack(side=BOTTOM)

Button(frameT, text="Red",fg="red").grid(column=1)
Button(frameT, text="Red2",fg="red").grid(column=2)
Button(frameM, text="Green",fg="green").grid(row=1)
Button(frameM, text="Green2",fg="green").grid(row=2)
Button(frameM, text="Green3",fg="green").grid(row=2,column=2)
Button(frameB, text="Blue",fg="blue").grid(row=1,column=1)
Button(frameB, text="Blue2",fg="blue").grid(row=1,column=2)


root.mainloop()