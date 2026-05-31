import os
import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import threading
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
SEARCH_URL = "https://api.pexels.com/v1/search"
CURATED_URL = "https://api.pexels.com/v1/curated"

HEADERS = {
"Authorization": PEXELS_API_KEY
}

class Gallery:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pexels Image Gallery")
        self.window.geometry("1100x700")
        self.window.tk_setPalette(
            background="#ffffff"
        )
        self.page = 1
        self.per_page = 9
        self.current_query = ""
        self.mode = "search"
        self.image_refs = []
        
        # Tkinter variables

        self.search_var = tk.StringVar(
            master=self.window
        )

        self.built_ui()

        self.window.mainloop()
    
    def built_ui(self):
        top_frame = tk.Frame(
            master=self.window,
            background="#ffffff"
        )
        top_frame.pack(fill="x", pady=15)

        title = tk.Label(
            master=top_frame,
            text="Pexels Image Gallery",
            font=("Arial", 25, "bold"),
            background="#ffffff"
        )
        title.pack(pady=(0, 10))

        control_frame = tk.Frame(
            master=top_frame,
        )
        control_frame.pack()

        control_frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")
        control_frame.rowconfigure((0,), weight=1, uniform="a")

        search_entry = ttk.Entry(
            master=control_frame,
            textvariable=self.search_var,
            font=("Arial", 20)
        )
        search_entry.grid(row=0, column=0, padx=(50, 8))

        search_entry.bind("<Return>", lambda event: self.search_images())

        search_btn = ttk.Button(
            master=control_frame,
            text="Search",
            command=self.search_images
        )
        search_btn.grid(row=0, column=1, padx=5)

        curated_btn = ttk.Button(
            master=control_frame,
            text="Trending/Curated"
        )
        curated_btn.grid(row=0, column=2, padx=5)

        next_btn = ttk.Button(
            master=control_frame,
            text="Next"
        )
        next_btn.grid(row=0, column=3, padx=5)

        clear_btn = ttk.Button(
            master=control_frame,
            text="Clear",
            command=self.clear_gallery
        )
        clear_btn.grid(row=0, column=4, padx=5)

        self.status_label = tk.Label(
            master=self.window,
            text="Search something to begin",
            font=("Arial", 15)
        )
        self.status_label.pack(pady=(0, 8))

        # Canvas

        canvas_frame = tk.Frame(
            master=self.window,
            background="#ffffff"
        )
        canvas_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.canvas = tk.Canvas(
            master=canvas_frame,
            background="#ffffff",
            highlightthickness=0
        )
        self.canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            master=canvas_frame,
            orient="vertical",
            command=self.canvas.yview
        )
        scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.gallery_frame = tk.Frame(
            master=self.canvas,
            background="#ffffff"
        )
        self.gallery_frame.bind("<Configure>", self.on_frame_configure)

        self.canvas_window = self.canvas.create_window((0, 0), window = self.gallery_frame, anchor="nw")
        
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # Mouse Wheel

        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)
    
    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)
    
    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def fetch_images(self):
        try:
            if self.mode == "search":
                params = {
                    "query": self.current_query,
                    "page": self.page,
                    "per_page": self.per_page
                }
                response = requests.get(SEARCH_URL, headers=HEADERS, params=params, timeout=20)
            else:
                params = {
                    "page": self.page,
                    "per_page": self.per_page
                }
                response = requests.get(CURATED_URL, headers=HEADERS, params=params, timeout=20)
            response.raise_for_status()
            data = response.json()
            photos = data.get("photos", [])
            if not photos:
                self.window.after(0, lambda:self.status_label.config(text="No images found"))
                return
            self.window.after(0, lambda:self.display_images(photos))
        except requests.exceptions.RequestException as e:
            self.window.after(0, lambda:messagebox.showerror("API Error: ", e))
            self.window.after(0, lambda:self.status_label.config(text="Error while fetching images"))
        except Exception as e:
            self.window.after(0, lambda:messagebox.showerror("Error: ", e))
            self.window.after(0, lambda:self.status_label.config(text="Unexpected error"))
    
    def fetch_images_threaded(self):
        self.clear_gallery()
        self.status_label.config(text="Fetching images...")
        threading.Thread(target = self.fetch_images, daemon=True).start()
    
    def display_images(self, photos):
        self.clear_gallery()
        column = 3
        card_width = 320
        for index, photo in enumerate(photos):
            row = index // column
            col = index % column
            card = tk.Frame(
                master=self.gallery_frame,
                background="#f0f0f0",
                bd=2
            )
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            image_url = photo["src"]["medium"]
            photographer = photo.get("photographer", "Pexels User")
            photo_alt = photo.get("alt", "Pexels Image")
            try:
                img_response = requests.get(image_url, timeout = 20)
                img_response.raise_for_status()
                pil_image = Image.open(BytesIO(img_response.content))
                pil_image.thumbnail((card_width, card_width))
                tk_image = ImageTk.PhotoImage(pil_image)
                self.image_refs.append(tk_image)
                img_label = tk.Label(
                    master=card,
                    image=tk_image,
                    background="#f0f0f0"
                )
                img_label.pack(padx=10, pady=10)
            
            except Exception as e:
                fallback = tk.Label(
                    master=card,
                    text="Image was not loaded",
                    background="#f0f0f0",
                    foreground="red"
                )
                fallback.pack(padx=10, pady=10)
            
            alt_label = tk.Label(
                master=card,
                text=photo_alt,
                wraplength=card_width-30,
                justify="center",
                font=("Arial", 12, "bold"),
                background="#f0f0f0"
            )
            alt_label.pack(padx=10, pady=(0, 10))

            photographer_label = tk.Label(
                master=card,
                text=f"Photo by: {photographer} of Pexels",
                wraplength=card_width-30,
                justify="center",
                font=("Arial", 10),
                background="#f0f0f0"
            )
            photographer_label.pack(padx=10, pady=(0, 10))

            if self.mode == "search":
                text = f"Showing page {self.page} results for '{self.current_query}'"
            else:
                text = f"Showing curated page {self.page} results"
            
            self.status_label["text"] = text

            self.canvas.yview("moveto", 0)
    
    def search_images(self):
        query = self.search_var.get().strip()
        if not query:
            messagebox.showwarning("Input Error", "Please enter a search term.")
            return
        self.current_query = query
        self.mode = "search"
        self.page = 1
        self.fetch_images_threaded()
    
    def clear_gallery(self):
        for widget in self.gallery_frame.winfo_children():
            widget.destroy()
        self.image_refs.clear()
        self.status_label["text"] = "Gallery cleared. Search something to begin."


if __name__ == "__main__":
    app = Gallery()