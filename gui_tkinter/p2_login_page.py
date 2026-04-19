import re
import string
import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.geometry("500x400")
window.title("Login")

# Functions and Classes
def field_validation():
    username = name_entry.get().strip()
    password = password_entry.get()

    username_pattern = r"^[A-Za-z]{5,}$"
    if not re.fullmatch(username_pattern, username):
        messagebox.showwarning("Username Alert", "Username must contain at least 5 characters with only letters")
    
    password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])\S{8,}$"
    if not re.fullmatch(password_pattern, password):
        messagebox.showwarning("Password Alert", "Password must contain one capital letter, one lowercase letter, one number, one special character, and no spaces")
        return
    
    messagebox.showinfo("Login", "You are logged in")
    name_entry.delete(0, "end")
    password_entry.delete(0, "end")

# Widgets
name_label = tk.Label(
    master=window,
    text="Username:",
    font=("Arial", 20, "bold"),
    background="#310A31",
    foreground="#FFFFFF",
    border=10
)
name_label.place(relx=0.05, rely=0.10, anchor="nw")
name_entry = tk.Entry(
    master=window,
    font=("Arial", 20, "bold"),
    background="#BA1F33",
    foreground="#FFFFFF",
    justify="center",
    insertbackground="#273469"
)
name_entry.place(relx=0.45, rely=0.125, anchor="nw", relwidth=0.50)
password_label = tk.Label(
    master=window,
    text="Password:",
    font=("Arial", 20, "bold"),
    background="#310A31",
    foreground="#FFFFFF",
    border=10
)
password_label.place(relx=0.05, rely=0.40, anchor="nw")
password_entry = tk.Entry(
    master=window,
    font=("Arial", 20, "bold"),
    background="#BA1F33",
    foreground="#FFFFFF",
    justify="center",
    insertbackground="#273469",
    show="*"
)
password_entry.place(relx=0.45, rely=0.425, anchor="nw", relwidth=0.50)
button = tk.Button(
    master=window,
    text="Submit",
    font=("Arial", 15, "bold"),
    background="#273C2C",
    foreground="#FFFFFF",
    border=5,
    command=field_validation
)
button.place(relx=0.5, rely=0.75, anchor="center")

window.mainloop()