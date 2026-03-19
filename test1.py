from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re

root = Tk()
root.title("Sign In")
root.geometry("900x550")
root.configure(bg="black")

try:
    logo_img = Image.open("logo.png")
    logo_img = logo_img.resize((120,120))
    logo = ImageTk.PhotoImage(logo_img)
except FileNotFoundError:
    print("Warning: logo.png not found. Running without logo.")
    logo = None

if logo:
    logo_label = Label(root, image=logo, bg="black")
    logo_label.pack(pady=20)

card = Frame(root, bg="#e6e6e6", width=420, height=320)
card.pack()
card.pack_propagate(False)

title = Label(card, text="Sign In", font=("Arial",20,"bold"), bg="#e6e6e6", fg="#444")
title.pack(anchor="w", padx=25, pady=(20,10))

email_entry = Entry(card, font=("Arial",13), width=32)
email_entry.pack(padx=25, pady=10, ipady=6)

password_entry = Entry(card, font=("Arial",13), width=32, show="*")
password_entry.pack(padx=25, pady=10, ipady=6)

var = IntVar()

check = Checkbutton(card, text="Keep me signed in", variable=var,
bg="#e6e6e6", font=("Arial",11))
check.pack(anchor="w", padx=25, pady=5)


def login():
    email = email_entry.get()
    password = password_entry.get()
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if email == "" or password == "":
        messagebox.showwarning("Error","Please fill all fields")
    elif not re.match(pattern,email):
        messagebox.showerror("Invalid Email","Enter valid email")
    else:
        messagebox.showinfo("Success","Login Successful")

btn = Button(card, text="Sign in", bg="#f4a300", fg="black",
font=("Arial",12,"bold"), width=12, command=login)
btn.pack(anchor="e", padx=25, pady=15)

root.mainloop()