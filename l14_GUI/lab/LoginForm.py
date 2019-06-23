from tkinter import *
from  tkinter import messagebox

def login():
    n=name.get()
    l=lastname.get()
    if(n=="Jacky" and l=="Chan"):
        messagebox.showinfo("Login Successful","Welcome to "+n)
    else:
        messagebox.showinfo("Login Failed","Try again")


def exitWindow():
    exit()

root = Tk()
#root.minsize(width=500,height=500)
root.title('Login Form')

Label(root,text='Name').grid(row=0)
Label(root,text='LastName').grid(row=1)

name = Entry(root)
name.grid(row=0,column=1)
lastname = Entry(root)
lastname.grid(row=1,column=1)

bLogin=Button(root,text="Login")
bLogin.grid(row=2,column=0)
bLogin.config(command=login)

bExit=Button(root,text="Exit")
bExit.grid(row=2,column=1)
bExit.config(command=exitWindow)

root.mainloop()