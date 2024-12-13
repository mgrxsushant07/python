import tkinter as tk
from tkinter import messagebox

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="white")

        self.expression = ""
        self.screen_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Display Screen
        screen = tk.Entry(self.root, textvar=self.screen_var, font="Arial 24 bold", bg="white", fg="black",
                           relief=tk.RAISED, borderwidth=3, justify=tk.RIGHT, insertbackground="black")
        screen.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="we")

        # Button Layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C","Clear", "0", "=", "+"]
        ]

        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                self.create_button(text, i + 1, j)

        # Configure row and column weights for responsiveness
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

        # Bind keyboard input
        self.root.bind("<Key>", self.key_press)

    def create_button(self, text, row, col):
        btn = tk.Button(self.root, text=text, font="Arial 15 bold", bg="#f0f0f0", fg="black",
                        padx=20, pady=20, relief=tk.RAISED, borderwidth=3, activebackground="#d9d9d9",
                        activeforeground="black")
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        btn.bind("<Button-1>", self.click)

    def click(self, event):
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = eval(self.expression)
                self.expression = str(result)
                self.screen_var.set(self.expression)
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.screen_var.set(self.expression)
        elif text == "C":
            self.expression = ""
            self.screen_var.set(self.expression)
        elif text == "Clear":
            self.expression = self.expression[:-1]
            self.screen_var.set(self.expression)
        else:
            self.expression += text
            self.screen_var.set(self.expression)

    def key_press(self, event):
        if event.char.isdigit() or event.char in "+-*/.=()":
            self.expression += event.char
            self.screen_var.set(self.expression)
        elif event.keysym == "Return":
            try:
                result = eval(self.expression)
                self.expression = str(result)
                self.screen_var.set(self.expression)
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.screen_var.set(self.expression)
        elif event.keysym == "BackSpace":
            self.expression = self.expression[:-1]
            self.screen_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ModernCalculator(root)
    root.mainloop()
