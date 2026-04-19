import tkinter as tk
import random

# Creating the window

window = tk.Tk()
window.title("Rolling the Dice Game")
window.geometry("550x425")
window.tk_setPalette("#121314")

# Variables and Tkinter variables

dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

# Functions

def select_dice():
    roll1 = random.choice(dice)
    roll2 = random.choice(dice)
    label1["text"] = roll1
    label2["text"] = roll2

# Widgets

button = tk.Button(
    master=window,
    text="Roll",
    font=("Arial", 14, "bold"),
    background="#242526",
    foreground="#ffffff",
    activebackground="#37393B",
    border=3,
    command=select_dice
)
button.pack(pady=10)

label1 = tk.Label(
    master=window,
    text="",
    font=("Arial", 100, "bold"),
    foreground="#ffffff",
    width=5
)
label1.place(relx=0.25, rely=0.5, anchor="center")

label2 = tk.Label(
    master=window,
    text="",
    font=("Arial", 100, "bold"),
    foreground="#ffffff",
    width=5
)
label2.place(relx=0.75, rely=0.5, anchor="center")

window.mainloop()