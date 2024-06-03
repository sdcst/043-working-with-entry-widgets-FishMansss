#!python3
import tkinter
from tkinter import *
import math
window = Tk()
window.geometry("400x80")
window.title("task 2")
"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""

def caclulate():
    l = elength.get()
    l = float(l)
    w = ewidth.get()
    w = float(w)
    h = (w**2 + l**2)**0.5
    h = round(h,2)
    h = str(h)
    eoutput.config(text=h)
    
llength=Label(window,text="length")
lwidth=Label(window,text="width")
elength=Entry(window)
ewidth=Entry(window)
eoutput=Label(window,text="             hypotenuse         ",background="grey")
button=Button(window,text="calculate",command=caclulate)

llength.grid(row=1,column=1)
lwidth.grid(row=1,column=2)
elength.grid(row=2,column=1)
ewidth.grid(row=2,column=2)
eoutput.grid(row=2,column=3)
button.grid(row=3,column=3)

window.mainloop()