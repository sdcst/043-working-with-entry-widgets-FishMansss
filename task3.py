#!python3

"""
Create the interface shown.  The program should be able to perform the math operation specified
by the buttons and display the entry in the 3rd entry widget;
"""
import math
import tkinter as tk
from tkinter.constants import END
import math

w = tk.Tk()
w.attributes("-topmost",True)

def mult(event):
    print(event)
    x = e[0].get()
    y = e[1].get()
    x = int(x)
    y = int(y)
    answer = x*y
    e[2].delete(0,tk.END)
    e[2].insert(0,answer)

def divi(event):
    print(event)
    x = e[0].get()
    y = e[1].get()
    x = int(x)
    y = int(y)
    answer = x/y
    e[2].delete(0,tk.END)
    e[2].insert(0,answer)
    
def addi(event):
    print(event)
    x = e[0].get()
    y = e[1].get()
    x = int(x)
    y = int(y)
    answer = x+y
    e[2].delete(0,tk.END)
    e[2].insert(0,answer)
    
def subt(event):
    print(event)
    x = e[0].get()
    y = e[1].get()
    x = int(x)
    y = int(y)
    answer = x-y
    e[2].delete(0,tk.END)
    e[2].insert(0,answer)
    

l = []
l.append( tk.Label(w,text="Number 1"))
l.append( tk.Label(w,text="Number 2"))
l.append( tk.Label(w,text="Number Calculator"))


e = []
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text="answer"))
b=[]
b.append(tk.Button(w,text="x"))
b.append(tk.Button(w,text="+"))
b.append(tk.Button(w,text="-"))
b.append(tk.Button(w,text="÷"))
b[0].bind("<Button-1>",mult)
b[1].bind("<Button-1>",addi)
b[2].bind("<Button-1>",subt)
b[3].bind("<Button-1>",divi)
l[2].grid(row=1,column=1,columnspan=4)
l[0].grid(row=2,column=1,columnspan=2)
l[1].grid(row=2,column=3,columnspan=2)
b[0].grid(row=3,column=1)
b[1].grid(row=3,column=2)
b[2].grid(row=3,column=3)
b[3].grid(row=3,column=4)
e[0].grid(row=4,column=1,columnspan=2)
e[1].grid(row=4,column=3,columnspan=2)
e[2].grid(row=4,column=5)
w.mainloop()
