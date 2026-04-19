import tkinter as tk
from tkinter import ttk, messagebox

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator App")
        self.window.geometry("700x600")
        self.window.tk_setPalette(background="#202020")
        # State variables
        self.first_no = ""
        self.current_no = ""
        self.operation = 0
        self.decimal_tracker = False
        # Calling Methods
        self.configure_grid()
        self.create_widgets()
    def configure_grid(self):
        self.window.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="a")
        self.window.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
    def create_widgets(self):
        self.number_input = tk.Entry(
            master=self.window,
            font=("Arial", 20, "bold"),
            background="#202020",
            foreground="#fefefe",
            insertbackground="#fefefe",
            justify="right",
            border=5
        )
        self.number_input.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=5,
            pady=5
        )
        # Number Buttons
        buttons_list = [
            [7, 8, 9],
            [4, 5, 6],
            [1, 2, 3],
            [0]
        ]
        for row_no, sub_list in enumerate(buttons_list, start=2):
            for col_no, number in enumerate(sub_list):
                button = tk.Button(
                    master=self.window,
                    text=number,
                    font=("Arial", 20, "bold"),
                    background="#141720",
                    foreground="#fefefe",
                    activebackground="#2F3652",
                    activeforeground="#DDDDDD",
                    border=3,
                    command=lambda number = number: self.numeric_click(number)
                )
                if number != 0:
                    button.grid(
                        row=row_no,
                        column=col_no,
                        padx=5,
                        pady=5,
                        sticky="nsew"
                    )
                else:
                    button.grid(
                        row=row_no,
                        column=col_no,
                        columnspan=2,
                        padx=5,
                        pady=5,
                        sticky="nsew"
                    )
        decimal_button = tk.Button(
            master=self.window,
            text=".",
            font=("Arial", 20, "bold"),
            background="#141720",
            foreground="#fefefe",
            activebackground="#2F3652",
            activeforeground="#DDDDDD",
            border=3,
            command=lambda: self.numeric_click(".")
        )
        decimal_button.grid(
            row=5,
            column=2,
            padx=5,
            pady=5,
            sticky="nsew"
        )

        # Arithmetic buttons

        add_button = tk.Button(
            master=self.window,
            text="+",
            font=("Arial", 20, "bold"),
            background="#141720",
            foreground="#fefefe",
            activebackground="#2F3652",
            activeforeground="#DDDDDD",
            border=3,
            command=lambda: self.calculation(1)
        )
        add_button.grid(
            row=4,
            column=3,
            padx=5,
            pady=5,
            sticky="nsew"
        )

        subtract_button = tk.Button(
            master=self.window,
            text="−",
            font=("Arial", 20, "bold"),
            background="#141720",
            foreground="#fefefe",
            activebackground="#2F3652",
            activeforeground="#DDDDDD",
            border=3,
            command=lambda: self.calculation(2)
        )
        subtract_button.grid(
            row=3,
            column=3,
            padx=5,
            pady=5,
            sticky="nsew"
        )

        multiply_button = tk.Button(
            master=self.window,
            text="×",
            font=("Arial", 20, "bold"),
            background="#141720",
            foreground="#fefefe",
            activebackground="#2F3652",
            activeforeground="#DDDDDD",
            border=3,
            command=lambda: self.calculation(3)
        )
        multiply_button.grid(
            row=2,
            column=3,
            padx=5,
            pady=5,
            sticky="nsew"
        )

        division_button = tk.Button(
            master=self.window,
            text="÷",
            font=("Arial", 20, "bold"),
            background="#141720",
            foreground="#fefefe",
            activebackground="#2F3652",
            activeforeground="#DDDDDD",
            border=3,
            command=lambda: self.calculation(4)
        )
        division_button.grid(
            row=1,
            column=3,
            padx=5,
            pady=5,
            sticky="nsew"
        )

        # Result button

        equals_button = tk.Button(
            master=self.window,
            text="=",
            font=("Arial", 20, "bold"),
            background="#141720",
            foreground="#fefefe",
            activebackground="#2F3652",
            activeforeground="#DDDDDD",
            border=3,
            command=self.result
        )
        equals_button.grid(
            row=5,
            column=3,
            padx=5,
            pady=5,
            sticky="nsew"
        )

        # Clear button

        clear_button = tk.Button(
            master=self.window,
            text="C",
            font=("Arial", 20, "bold"),
            background="#141720",
            foreground="#fefefe",
            activebackground="#2F3652",
            activeforeground="#DDDDDD",
            border=3,
            command=self.clear
        )
        clear_button.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="nsew"
        )

        # Backspace

        backspace_button = tk.Button(
            master=self.window,
            text="⌫",
            font=("Arial", 20, "bold"),
            background="#141720",
            foreground="#fefefe",
            activebackground="#2F3652",
            activeforeground="#DDDDDD",
            border=3,
            command=self.backspace
        )
        backspace_button.grid(
            row=1,
            column=2,
            padx=5,
            pady=5,
            sticky="nsew"
        )

    def update_display(self, value):
        self.number_input.delete(0, "end")
        self.number_input.insert(0, value)
    
    def numeric_click(self, num):
        if num == ".":
            if not self.decimal_tracker:
                self.decimal_tracker = True
                self.current_no += "."
        else:
            self.current_no += str(num)
        self.update_display(self.current_no)
    
    def backspace(self, event=None):
        if self.current_no:
            if self.current_no[-1] == ".":
                self.decimal_tracker = False
            self.current_no = self.current_no[:-1]
        self.update_display(self.current_no)
    
    def bind_events(self):
        self.window.bind("<BackSpace>", self.backspace)

    def clear(self):
        self.first_no = ""
        self.current_no = ""
        self.operation = 0
        self.decimal_tracker = False
        self.update_display("")

    def calculation(self, op_num):
        if not self.current_no:
            messagebox.showerror("Error", "Enter a number first")
            return
        self.first_no = self.current_no
        self.current_no = ""
        self.decimal_tracker = False
        self.operation = op_num
        self.update_display("")
    
    def result(self):
        if not self.first_no and not self.operation:
            messagebox.showerror("Error", "Enter a number and then an operation")
            return
        if not self.current_no:
            messagebox.showerror("Error", "Enter second number")
            return
        num1 = float(self.first_no)
        num2 = float(self.current_no)
        if self.operation == 1:
            result = num1 + num2
        elif self.operation == 2:
            result = num1 - num2
        elif self.operation == 3:
            result = num1 * num2
        elif self.operation == 4:
            try:
                result = num1 / num2
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        formatted = f"{result:.4f}"
        self.update_display(formatted)

        self.first_no = formatted
        self.current_no = formatted
        self.decimal_tracker = "." in formatted
        self.operation = 0

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()