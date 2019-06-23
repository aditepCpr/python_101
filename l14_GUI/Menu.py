from tkinter import *
from tkinter import Menu

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    # Canvas
    cv = Canvas(root, bg="blue", height=250, width=300)
    cv.pack()

    button.pack()

root = Tk()
root.title('App with Menu')
root.minsize(width=300,height=300)
menubar = Menu(root)
#######################################################################
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
########################################################################

root.config(menu=menubar)
root.mainloop()