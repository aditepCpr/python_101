from tkinter import *

root = Tk()
root.title('Hello My Form')
root.minsize(width=800, height=800)


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

# bottom = Label(p2, text="bottom pane")

labelframe = LabelFrame(p2, text="this is a LabelFrame")
labelframe.pack()

left = Label(labelframe,text="inside the LabelFrame")
left.pack()
p2.add(labelframe)

# p2.add(bottom)



root.mainloop()
