import tkinter as tk
from tkinter import *
 
root=tk.Tk()
l1=tk.Label(root,text="Regno")
l1.grid(row=0)
t1=tk.Entry(root)
t1.grid(row=0,column=1)
l2=tk.Label(root,text="Name:")
l2.grid(row=1)
t2=tk.Entry(root)
t2.grid(row=1,column=1)
l3=tk.Label(root,text="Dept")
l3.grid(row=2)
t3=tk.Entry(root)
t3.grid(row=2,column=1)
gender=IntVar()
def gen():
    print(gender.get())
g=tk.Label(root,text="Gender")
g.grid(row=3,column=0)
g1=Radiobutton(root,text="Male",variable=gender,width=25,value=1,command=gen)
g1.grid(row=3,column=1)
g2=Radiobutton(root,text="Female",variable=gender,width=25,value=2,command=gen)
g2.grid(row=3,column=2)
age=tk.Label(root,text="Age")
age.grid(row=4,column=0)
age=Spinbox(root,from_=0, to = 30)
age.grid(row=4,column=1)
insert=tk.Button(root,text="Insert",width=5,command=root.destroy)
insert.grid(row=5,column=0)
update=tk.Button(root,text="Update",width=5,command=root.destroy)
update.grid(row=5,column=1)
delete=tk.Button(root,text="Delete",width=5,command=root.destroy)
delete.grid(row=6,column=0)
select=tk.Button(root,text="Select",width=5,command=root.destroy)
select.grid(row=6,column=1)
 
root.mainloop()