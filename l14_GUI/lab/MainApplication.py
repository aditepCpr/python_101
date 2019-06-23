import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.title("Main application")

root.minsize(width=300, height=300)


def donothing():
    pass


def openLogin():
    global tl
    tl = Toplevel(root)
    global name
    name = Entry(tl)
    global lastname
    lastname = Entry(tl)
    bLogin = Button(tl, text="Login")
    bExit = Button(tl, text="close")

    Label(tl, text='Name').grid(row=0)
    Label(tl, text='LastName').grid(row=1)
    name.grid(row=0, column=1)
    lastname.grid(row=1, column=1)

    bLogin.grid(row=2, column=0)
    bLogin.config(command=login)
    bExit.grid(row=2, column=1)
    bExit.config(command=lambda: closeForm(tl))


def closeForm(form):
    form.destroy()


def login():
    n = name.get()
    l = lastname.get()
    if (n == "Jacky" and l == "Chan"):
        messagebox.showinfo("Login Successful", "Welcome to " + n)
        tl.destroy()
    else:
        messagebox.showinfo("Login Failed", "Try again")


def exitWindow():
    exit()


def helpinfo():
    global th
    global img
    th = Toplevel(root)
    frameT = Frame(th)
    frameM = Frame(th)
    frameB = Frame(th)
    th.minsize(width=500, height=500)

    frameT.config(width=500, height=100)
    frameT.pack(side=TOP)

    frameM.config(width=500, height=100)
    frameM.pack()
    frameB.config(width=500, height=100)
    frameB.pack(side=BOTTOM)
    # Button(frame, text="Red", fg="red").grid(column=1)

    cv = Canvas(frameT, height=250, width=100)
    cv.create_text(50, 50, text="My Application")

    cv.pack()

    cv2 = Canvas(frameM, bg="blue", height=200, width=200)
    img = PhotoImage(file="python.png")
    cv2.create_image(10,10, image=img)
    cv2.pack()


    cv3 = Canvas(frameB, height=100, width=100)
    cv3.create_text(50, 50, text="Copy @2019")
    cv3.pack()

menubar = Menu(root)

fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label="Login", command=openLogin)
fileMenu.add_command(label="Open", command=donothing)
fileMenu.add_command(label="Save", command=donothing)
fileMenu.add_command(label="Close", command=donothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitWindow)
menubar.add_cascade(label='File', menu=fileMenu)

editMenu = Menu(menubar, tearoff=0)
editMenu.add_command(label='Undo', command=donothing)
editMenu.add_separator()
editMenu.add_command(label="Cut", command=donothing)
editMenu.add_command(label="Paste", command=donothing)
editMenu.add_command(label="Delete", command=donothing)
editMenu.add_command(label="Exit", command=donothing)
menubar.add_cascade(label='Edit', menu=editMenu)

HelpMenu = Menu(menubar, tearoff=0)
HelpMenu.add_command(label="Help", command=helpinfo)
HelpMenu.add_separator()
HelpMenu.add_command(label="Update Version", command=donothing)
HelpMenu.add_command(label="About", command=donothing)
menubar.add_cascade(label='Help', menu=HelpMenu)

root.config(menu=menubar)
root.mainloop()
