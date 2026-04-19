import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.geometry("500x500")
window.title("Multiplication Table")
window.tk_setPalette(background = "#2e3440")

# Icon

icon = tk.PhotoImage(file = "gui_tkinter/assets/settings-sliders.png")
window.iconphoto(True, icon)

# Functions

frame = None

def table_calculator():
    global frame
    if frame:
        frame.destroy()
    try:
        num = int(entry.get())
        info_label["text"] = f"Multiplication Table for {num:02d}:"
        frame = tk.Frame(
            master=window,
            background="#4b7fb9",

        )
        frame.place(relx=0.05, rely=0.40, relwidth=0.90, relheight=0.55)

        y = 0.07
        for i in range(1, 11):
            f_label =  tk.Label(
                master=frame,
                text=f"{num} x {i} = {num * i}",
                background="#696f7e",
                font=("Arial", 9, "bold"),
                foreground="#FFF", 
                border=10
            )
            f_label.place(relx=0.50, rely=y, anchor="center", relwidth=0.75)
            y += 0.095
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Widgets

label = tk.Label(
    master=window,
    text="Enter a number to display its Table",
    background="#88bd81",
    foreground="#FFF", 
    border=10,
    wraplength=150
)
label.place(relx=0.05, rely=0.075)

entry = tk.Entry(
    master=window,
    background="#2a2d2e",
    foreground="#FFFFFF",
    font=("Arial", 15, "bold"),
    justify="center", border=5
)
entry.place(relx=0.40, rely=0.10, relwidth=0.35)

button = tk.Button(
    master=window,
    text="Show Table",
    background="#88bd81",
    font=("Arial", 11, "bold"),
    foreground="#DDD", 
    border=5,
    command=table_calculator
)
button.place(relx=0.775, rely=0.095)

info_label = tk.Label(
    master=window,
    text="",
    background="#2e3440",
    font=("Arial", 9, "bold"),
    foreground="#FFF", 
    border=10
)
info_label.place(relx=0.50, rely=0.25, anchor="center")

sep_label =  tk.Label(
    master=window,
    text="",
    background="#2e3440",
    font=("Arial", 9, "bold"),
    foreground="#FFF", 
    border=10
)
sep_label.place(relx=0.50, rely=0.35, anchor="center")

window.mainloop()