# GUI

```
Tkinter " standard GUI library "
มีหลาย lib เช่น JPython wxPython

Provide a fast and easy way to create GUI application

Provides a powerful object-oriented interface to the Tk GUI toolkit

East Steps :
1. Import The Tkinter module.
2. Create the GUI application main window.
3. Add one or more of the above-mentioned widgets to the GUI application
4. Enter the main event loop to take action against each event triggered by the user.

```

```python
import tkinter
top = tkinter.Tk()
# Code to add widgets will fo here...
top.mainloop()

```
```python
from tkinter import *
from tkinter import messagebox
def button_click():
        messagebox.showinfo("Say Hello","Hello World")


root = Tk()

b = Button(root,text = 'OK')
b.config(fg='red',bg='yellow',bd=4 )
b.config(width=10,height=3)
b.config(command=button_click)
b.pack()

root.mainloop()



```
### Entry 
``` 
# get() ดึงค่า  # insert(index,s) แทรกข้อความ # delete(first,last=None) ลบข้อความ  index(index)
```
```
# Option
bg , fg , command ,font , height , width ,text ,state , bd ,show

```
```python
from tkinter import *
from tkinter import messagebox


def button_click():
    name=e1.get()
    last=e2.get()
    messagebox.showinfo("Sqy Hello","Hello World :"+name+" "+last)

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

root.mainloop()s

```
### Frame
``` 
Options

bg , bd , cursor , height , width

```
` frame.pack(side=TOP)  rame.pack(side=BOTTOM)  rame.pack(side=LEFT)  rame.pack(side=RIGHT)  `
```python
from tkinter import *

root = Tk()
frame = Frame(root)
frame.config(width=500,height=400,bg="blue")
frame.pack()
root.mainloop()

```
### PanelWindow
```
Methods
add(child,option)
get(startIbdex,endIndex)
config(option)
```
```python
from tkinter import *

root = Tk()
root.title('Hello My Form')
root.minsize(width=270, height=120)

p1 = PanedWindow(bg='red')
p1.pack(fill=BOTH, expand=1)

left = Label(p1, text="left pane")
bLeft = Button(p1, text="Red", fg='red')
p1.add(left)
p1.add(bLeft)

p2 = PanedWindow(p1, bg='green', orient=VERTICAL)
p1.add(p2)

top = Label(p2, text="top pane")
p2.add(top)
p2.add(Button(p2, text="Green", fg="green"))

bottom = Label(p2, text="bottom pane")
p2.add(bottom)

root.mainloop()

```
### LabelFrame

```python
labelframe = LabelFrame(p2, text="this is a LabelFrame")
labelframe.pack()

left = Label(labelframe,text="inside the LabelFrame")
left.pack()
p2.add(labelframe)

```

### Menu 
``` 
Methods

add_command(option)
add_separator()
add_radiobutton(ops)
add_checkbutton(ops) # editmenu.add_checkbutton(label="undo")
add_cascade(ops)       

```
```python
from tkinter import *
from tkinter import Menu

root = Tk()
root.title('App with Menu')
root.minsize(width=300,height=300)
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command=donothing)
filemenu.add_checkbutton(label="Open")
filemenu.add_radiobutton(label="Save",command=donothing)
filemenu.add_command(label="Save as..",command=donothing)
filemenu.add_command(label="Close",command=donothing)

filemenu.add_separator() # --------------- #

filemenu.add_command(label="Exit",command=root.quit)
filemenu.add_checkbutton(label="undo")
menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)
root.mainloop()

```
### Menu Buttom
```python
mb = Menubuttom (root,text="Menu Button",relief=RAISED)
mb.grid()
mb.memu = Menu (mb , tearoff = 0)
mb["Menu"] = mb.menu

mb.memu.add_checkbutton (label="mayo")
mb.menu.add_checkbutton (label="hetchup")

mb.pack()

```

### Canvas
```
creat_XXX() oval,arc,image,line,oval,polygon,text,tectangle
```
```python
from tkinter import *

root = Tk()
root.title("My Canvas")
root.minsize(width=500 ,height= 500)
cv = Canvas(root, bg="bule",height=250 ,width=300)

cv.pack()
root.mainloop()

```