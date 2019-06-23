from tkinter import *
from tkinter import messagebox


def button_click():
    name=e1.get()
    last=e2.get()
    messagebox.showinfo("Sqy Hello","Hello World :"+name+" "+last)

def clear():
    e1.delete(0,len(e1.get()))
    e2.delete(0,len(e2.get()))

root = Tk()
Label(root,text='First Name').grid(row=0)
Label(root,text='Last Name').grid(row=1)
e1 = Entry(root) # ช่อง input
e2 = Entry(root)

# get() ดึงค่า  # insert(index,s) แทรกข้อความ # delete(first,last=None) ลบข้อความ
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b = Button(root,text='ok')
b.grid(row=2)
b.config(command=button_click)
Button(root,text='clear',command=clear).grid(row=2,column=1)

root.mainloop()