import tkinter as tk
from tkinter import ttk, messagebox

# Creating window

class TravelApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Travel Booking App")
        self.window.geometry("600x480")
        self.window.resizable(False, False)
        self.window.tk_setPalette(background="white")

        self.destination = tk.StringVar(master=self.window)
        self.hotel_suite = tk.BooleanVar(master=self.window)
        self.spa = tk.BooleanVar(master=self.window)
        self.safari = tk.BooleanVar(master=self.window)
        self.scuba_diving = tk.BooleanVar(master=self.window)
        self.progress_value = 0

        self.create_booking_screen()
        self.window.mainloop()
    
    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def create_booking_screen(self):
        self.clear_screen()
        title = tk.Label(
            master=self.window,
            text="Travel Booking App",
            font=("Arial", 22, "bold"),
            background="#ffffff",
            foreground="black"
        )
        title.pack(pady=20)

        main_frame = tk.Frame(
            master=self.window,
            background="#fefefe"
        )
        main_frame.pack(pady=(0, 10))

        # Destination section

        d_frame = tk.LabelFrame(
            master=main_frame,
            text="Select Flight Destination",
            font=("Arial", 14, "bold"),
            padx=20,
            pady=50
        )
        d_frame.grid(row=0, column=0, padx=15)

        destinations = ["Goa", "Pattaya", "Bali", "Hawaii"]

        for place in destinations:
            radio = tk.Radiobutton(
                master=d_frame,
                text=place,
                variable=self.destination,
                value=place,
                font=("Arial", 12)
            )
            radio.pack(anchor="w")
        
        booking_frame = tk.LabelFrame(
            master=main_frame,
            text="Flight Booking Add-Ons",
            font=("Arial", 14, "bold"),
            padx=20,
            pady=15
        )
        booking_frame.grid(row=0, column=1, padx=15)

        c1 = tk.Checkbutton(
            master=booking_frame,
            text="Hotel Suite",
            variable=self.hotel_suite,
            font=("Arial", 12)
        )
        c1.pack(anchor="w")

        c2 = tk.Checkbutton(
            master=booking_frame,
            text="Spa",
            variable=self.spa,
            font=("Arial", 12)
        )
        c2.pack(anchor="w")

        c3 = tk.Checkbutton(
            master=booking_frame,
            text="Jungle Safari",
            variable=self.safari,
            font=("Arial", 12)
        )
        c3.pack(anchor="w")

        c4 = tk.Checkbutton(
            master=booking_frame,
            text="Scuba Diving",
            variable=self.scuba_diving,
            font=("Arial", 12)
        )
        c4.pack(anchor="w")

        self.submitbutton = tk.Button(
            master=self.window,
            text="Book Ticket",
            font=("Comic Sans MS", 14, "bold"),
            background="#fefefe",
            command=self.start_booking
        )
        self.submitbutton.pack(pady=25)

        self.progress = ttk.Progressbar(
            master=window,
            orient="horizontal",
            length=350,
            mode="determinate"
        )

    def start_booking(self):
        if not self.destination.get():
            messagebox.showwarning("Destination required", "Please select a flight destination")
            return
        self.submitbutton.config(state="disabled")
        self.progress.pack(pady=10)
        self.progress_value = 0
        self.progress["value"] = 0
        self.load_progress()
        
    def load_progress(self):
        if self.progress_value < 100:
            self.progress_value += 1
            self.progress["value"] = self.progress_value
            self.window.after(100, self.load_progress)
        else:
            self.show_confirmation()

    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def show_confirmation(self):
        self.clear_screen()
        selected_services = []
        if self.hotel_suite.get():
            selected_services.append("Hotel Suite")
        if self.spa.get():
            selected_services.append("Spa")
        if self.safari.get():
            selected_services.append("Jungle Safari")
        if self.scuba_diving.get():
            selected_services.append("Scuba Diving")
        if selected_services:
            services_text = ", ".join(selected_services)
        else:
            services_text = "No extra services selected"
        label1 = tk.Label(
            master=self.window,
            text="Booking Confirmed",
            font=("Arial", 24, "bold")
            background="#fefefe"
        )
        label1.pack(pady=20)

        label2 = tk.Label(
            master=self.window,
            text="Your tickets have been book successfully",
            font=("Arial", 14, "bold")
            background="#fefefe"
        )
        label2.pack(pady=10)

        ticket_frame = tk.Frame(
            master=self.window,
            background="#fefefe",
        )
        ticket_frame.pack(pady=15)



if __name__ == "__main__":
    window = tk.Tk()
    app = TravelApp(window)