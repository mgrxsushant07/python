try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    raise ImportError("The tkinter library is not available. Please ensure it is installed or use an alternative GUI library.")

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            expression = str(result)
            screen_var.set(expression)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            screen_var.set(expression)
    elif text == "C":
        expression = ""
        screen_var.set(expression)
    else:
        expression += text
        screen_var.set(expression)

# Create the main Tkinter window
root = tk.Tk()
root.title("Calculator")

expression = ""
screen_var = tk.StringVar()
screen_var.set(expression)

# Create the screen widget
screen = tk.Entry(root, textvar=screen_var, font="Arial 20", borderwidth=5, relief=tk.SUNKEN)
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# Create button text layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Add buttons to the window
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        button = tk.Button(root, text=text, font="Arial 15", padx=20, pady=20, borderwidth=5)
        button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        button.bind("<Button-1>", click)

# Add grid weight for resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()