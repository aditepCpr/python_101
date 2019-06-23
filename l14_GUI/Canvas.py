import tkinter as tk
from tkinter import *
from tkinter import Canvas
from tkinter import messagebox

from sympy import fibonacci

root = Tk()
root.title('My Canvas')
root.minsize(width=500,height=500)
################################################
################### Canvas #####################
cv = Canvas(root,bg="blue",height=400,width=400)

cv.create_line(0,0,100,100,fill='red')
cv.create_line(50,50,50,400,fill="yellow",dash=(4,2))
cv.create_rectangle(50,25,150,75,fill='pink')
cv.create_polygon(150,150,150,200,150,200,100,200,fill='black')
cv.create_polygon(150,150,150,200,150,200,100,200,50,120,fill='black')
cv.create_polygon(150,150,150,200,150,200,100,200,50,120,80,120,fill="black")

cv.create_oval(200,200,250,250,width=2,outline="yellow",fill='green')
cv.create_oval(100,80,250,120, fill="green")

cv.create_text(20,30,anchor='center',font="Parisa",text="Most relationships seen so transitory")

img = PhotoImage(file = "python.png")
cv.create_image(300, 300, image=img, anchor='center')
cv.pack()
################################################
root.mainloop()
