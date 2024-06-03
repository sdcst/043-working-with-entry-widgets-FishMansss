import tkinter
from tkinter import *
import math
"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
window = Tk()
window.geometry("400x70")
window.title("task 1")

def state():
    name = ename.get()
    name = str(name)
    student = estudent.get()
    student = str(student)
    grade = egrade.get()
    grade = str(grade)
    output.config(text=f"grade = {grade}, name = {name}, student = {student}")

lname = Label(window,text="name")
lstudent = Label(window, text="student number")
lgrade = Label(window,text="grade")

ename = Entry(window)
estudent = Entry(window)
egrade = Entry(window)

output = Label(window,text="output...",background="grey")
button = Button(window,text="display",command=state)

########

lname.grid(column=1,row=1)
lstudent.grid(column=2,row=1)
lgrade.grid(column=3,row=1)
ename.grid(column=1,row=2)
estudent.grid(column=2,row=2)
egrade.grid(column=3,row=2)
button.grid(column=1,row=3)
output.grid(column=2,row=3,columnspan=2)

window.mainloop()