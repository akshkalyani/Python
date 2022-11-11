import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
l1 = tk.Label(root, text="Hello label1", font="Calibri").grid(row=5,column=1)
def button():
    b1.configure(text="Button clicked", bg="red")

b1=tk.Button(root, text = "Button1 Click",width=25, command=button, bg="red", fg="blue").grid(row=1,column=1)
# b1.pack()
c1=tk.Checkbutton(root, text="Check this", width=10).grid(row=3, column=1)

# Scrolledtext
# s1=tk.ScrolledText(text="Hello World in the scrolled Text", width=40, height=10).grid(row=8, column=1)

# messagebox
def clickFun():
    messagebox.showinfo('Message Title', 'Message Info')
msg1 = tk.Button(text="Message box open", width=10, command=clickFun).grid(row=9,column=1)
root.mainloop()
