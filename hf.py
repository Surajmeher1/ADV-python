from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("300x200")

def fun():
    messagebox.showinfo("Hello", "Blue Button clicked")

btn1 = Button(top, text="Red", bg="red", fg="white", width=10)
btn1.pack(side=LEFT)

btn2 = Button(top, text="Green", bg="green", fg="white", width=10, height=5,
activebackground="yellow")
btn2.pack(side=TOP)

btn3 = Button(top, text="Blue", bg="blue", fg="white", padx=10, pady=10,
command=fun)
btn3.pack(side=BOTTOM)

top.mainloop()