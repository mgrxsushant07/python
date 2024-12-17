# write a python program using Tkinter function to create a application that can convert temperature between Celsius, Fahrenheit, and Kelvin.

import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temp = float(entry_temperature.get())
        from_unit = combo_from_unit.get()
        to_unit = combo_to_unit.get()

        if from_unit == to_unit:
            result = temp
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (temp * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = temp + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (temp - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (temp - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = temp - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (temp - 273.15) * 9/5 + 32

        label_result.config(text=f"Converted Temperature: {result:.2f} {to_unit}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter a number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.configure(bg="lightblue")

# Input temperature
label_input = tk.Label(root, text="Enter Temperature:", bg="lightblue")
label_input.pack(pady=5)

entry_temperature = tk.Entry(root, width=20)
entry_temperature.pack(pady=5)

# Dropdown to select from-unit
label_from_unit = tk.Label(root, text="From:", bg="lightblue")
label_from_unit.pack(pady=5)

combo_from_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_from_unit.set("Celsius")
combo_from_unit.pack(pady=5)

# Dropdown to select to-unit
label_to_unit = tk.Label(root, text="To:", bg="lightblue")
label_to_unit.pack(pady=5)

combo_to_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_to_unit.set("Fahrenheit")
combo_to_unit.pack(pady=5)

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert_temperature)
button_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
label_result.pack(pady=10)

# Run the application
root.mainloop()
