import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import qrcode
from pathlib import Path

# Creating the window

window = tk.Tk()
window.title("QR Code Generator")
window.geometry("600x600")
window.tk_setPalette(background = "#212121")

# Functions

image = True
def generateQR():
    global image
    name = theme_entry.get().strip()
    url = url_entry.get().strip()
    try:
        qr = qrcode.make(url)
        file = f"{name}.png"
        save_folder = Path(__file__).parent / "qr_codes"
        save_folder.mkdir(exist_ok=True)
        file_path = save_folder / f"{name}.png"
        qr.save(file_path)
        image = tk.PhotoImage(file=file_path)
        image_label["image"] = image
        messagebox.showinfo("Success!", "QR Code saved")
    except Exception as e:
        messagebox.showerror("Error: ", f"An error occurred: {e}")

# Widgets

frame = tk.Frame(master=window)
frame.pack(fill="both", pady="20")

label = tk.Label(
    master=frame,
    text="QR Code Generator",
    background="#ffffff",
    foreground="black",
    font=("Arial", 16, "bold")
)
label.pack(pady=(10, 5))

theme_label = tk.Label(
    master=frame,
    text="Name your QR code",
    background="#ffffff",
    foreground="black",
    font=("Arial", 14, "bold")
)
theme_label.pack(pady=(10, 5))

theme_entry = tk.Entry(
    master=frame,
    font=("Arial", 14),
    justify="center"
)
theme_entry.pack(pady=(10, 5))

url_label = tk.Label(
    master=frame,
    text="Enter URL",
    background="#ffffff",
    foreground="black",
    font=("Arial", 14, "bold")
)
url_label.pack(pady=(10, 5))

url_entry = tk.Entry(
    master=frame,
    font=("Arial", 14),
    justify="center"
)
url_entry.pack(pady=(10, 5))

button = ttk.Button(
    master=frame,
    text="Generate QR",
    command=generateQR
)
button.pack(pady=(10, 5))

image_frame = tk.Frame(master=window)
image_frame.pack()

image_label = tk.Label(master=image_frame,)
image_label.pack()

window.mainloop()