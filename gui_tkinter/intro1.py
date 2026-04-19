import tkinter as tk
from tkinter import ttk, messagebox

# Creating a window

window = tk.Tk()
window.title("First App")
window.geometry("400x300")
window.tk_setPalette(background = "#1e1e1e")

# Variables and Tkinter Variables

# Functions or classes

def show_info():
    text = entry.get()
    messagebox.showinfo("Button clicked!", text)

# Create widgets

label = ttk.Label(
    master = window,
    text = "Welcome to My App",
    font = ("Arial", 20, "bold underline"),
    background = "blue",
    foreground = "white",
    border = 5
)

label.pack(pady = 10)

entry = ttk.Entry(
    master = window,
    font = ("Arial", 12, "bold"),
    justify = "center"
)

entry.pack(pady = (5, 10))

button = ttk.Button(master = window, text = "Click Me!", command = show_info)
button.pack()

window.mainloop()