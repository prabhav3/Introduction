import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("400x400")

window.title("Digital Clock")

icon = tk.PhotoImage(file = "gui_tkinter/assets/clock.png")
window.iconphoto(True, icon)

def display_dt():
    time_now = datetime.datetime.now()

    # Extract the string date

    date_label["text"] = time_now.strftime("%y/%m/%d - %A")
    time_label["text"] = time_now.strftime("%I:%M:%S %p")

    window.after(1000, display_dt)

# Widgets

date_img = ImageTk.PhotoImage(Image.open("gui_tkinter/assets/calendar.png"))

date_info = tk.Label(
    master = window,
    text = "Today's Date is: ",
    image = date_img,
    compound = "left",
    font = ("Arial", 25),
    padx = 18,
    pady = (10)
)

date_info.Image = date_img

date_info.pack()

date_label = tk.Label(
    master = window,
    text = "",
    font = ("Arial", 25)
)

date_label.pack()

time_img = ImageTk.PhotoImage(Image.open("gui_tkinter/assets/hourglass.png"))

time_info = tk.Label(
    master = window,
    text = "The Time is: ",
    image = time_img,
    compound = "left",
    font = ("Arial", 25),
    padx = 18,
    pady = (10)
)

time_info.Image = time_img

time_info.pack()

time_label = tk.Label(
    master = window,
    text = "",
    font = ("Arial", 25)
)

time_label.pack()

display_dt()
window.mainloop()