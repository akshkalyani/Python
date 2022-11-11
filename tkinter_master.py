from tkinter import *
 
def addNumbers():
    res=int(e1.get())+int(e2.get())
    myText.set(res)
    
def subNumbers():
    res=int(e1.get())-int(e2.get())
    myText.set(res)
    
def mulNumbers():
    res=int(e1.get())*int(e2.get())
    myText.set(res)
 
master = Tk()
myText=StringVar()
Label(master, text="First").grid(row=0)
Label(master, text="Second").grid(row=1)
Label(master, text="Result:").grid(row=3)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1)
 
e1 = Entry(master)
e2 = Entry(master)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
 
b = Button(master, text="ADD", command=addNumbers)
b.grid(row=0, column=2)

b = Button(master, text="SUB", command=subNumbers)
b.grid(row=1, column=2)

b = Button(master, text="MUL", command=mulNumbers)
b.grid(row=3, column=2)
 
mainloop()
