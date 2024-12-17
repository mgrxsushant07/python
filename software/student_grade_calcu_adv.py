import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to calculate GPA
def calculate_gpa():
    try:
        # Get marks for each subject from the entries
        math_marks = int(entry_math.get())
        science_marks = int(entry_science.get())
        optional_marks = int(entry_optional.get())  # Get marks for the selected optional subject
        nepali_marks = int(entry_nepali.get())
        english_marks = int(entry_english.get())
        social_marks = int(entry_social.get())
        computer_marks = int(entry_computer.get())
        
        # Validation for marks greater than 100 or negative marks
        if (math_marks > 100 or math_marks < 0 or
            science_marks > 100 or science_marks < 0 or
            optional_marks > 100 or optional_marks < 0 or
            nepali_marks > 100 or nepali_marks < 0 or
            english_marks > 100 or english_marks < 0 or
            social_marks > 100 or social_marks < 0 or
            computer_marks > 50 or computer_marks < 0):
            messagebox.showerror("Input Error", "Marks should be between 0 and 100 for all subjects (Computer full marks 50).")
            return

        # List of all marks to calculate average
        marks = [math_marks, science_marks, optional_marks, nepali_marks, english_marks, social_marks, computer_marks]
        
        # Calculate total and average
        total_marks = sum(marks)
        average = total_marks / len(marks)
        
        # Calculate GPA based on average (assuming a simple GPA scale)
        if average >= 90:
            gpa = 4.0
        elif average >= 80:
            gpa = 3.7
        elif average >= 70:
            gpa = 3.3
        elif average >= 60:
            gpa = 3.0
        elif average >= 50:
            gpa = 2.7
        elif average >= 40:
            gpa = 2.0
        else:
            gpa = 1.0
        
        # Display the GPA in the label
        label_result.config(text=f"Total Marks: {total_marks}\nAverage Marks: {average:.2f}\nGPA: {gpa:.2f}")
    except ValueError:
        # Show an error message if the input is invalid
        messagebox.showerror("Input Error", "Please enter valid marks for all subjects.")

# Function to increase or decrease marks with arrow buttons
def change_marks(entry_field, increment):
    try:
        current_value = int(entry_field.get())
        new_value = current_value + increment
        # Validation to ensure marks stay within bounds
        if new_value <= 100 and new_value >= 0:
            entry_field.delete(0, tk.END)
            entry_field.insert(0, str(new_value))
    except ValueError:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "0")

# Create the main window
root = tk.Tk()
root.title("Student Grade Calculator")

# Set background color for the window
root.configure(bg="#f0f8ff")

# Create labels for each subject
label_math = tk.Label(root, text="Mathematics:", bg="#f0f8ff", font=("Arial", 12))
label_math.grid(row=0, column=0, padx=10, pady=5)

label_science = tk.Label(root, text="Science:", bg="#f0f8ff", font=("Arial", 12))
label_science.grid(row=1, column=0, padx=10, pady=5)

label_optional = tk.Label(root, text="Optional Subject:", bg="#f0f8ff", font=("Arial", 12))
label_optional.grid(row=2, column=0, padx=10, pady=5)

label_nepali = tk.Label(root, text="Nepali:", bg="#f0f8ff", font=("Arial", 12))
label_nepali.grid(row=3, column=0, padx=10, pady=5)

label_english = tk.Label(root, text="English:", bg="#f0f8ff", font=("Arial", 12))
label_english.grid(row=4, column=0, padx=10, pady=5)

label_social = tk.Label(root, text="Social Studies:", bg="#f0f8ff", font=("Arial", 12))
label_social.grid(row=5, column=0, padx=10, pady=5)

label_computer = tk.Label(root, text="Computer (50 Marks):", bg="#f0f8ff", font=("Arial", 12))
label_computer.grid(row=6, column=0, padx=10, pady=5)

# Create entry fields for each subject
entry_math = tk.Entry(root, font=("Arial", 12))
entry_math.grid(row=0, column=1, padx=10, pady=5)

entry_science = tk.Entry(root, font=("Arial", 12))
entry_science.grid(row=1, column=1, padx=10, pady=5)

# Create dropdown (ComboBox) for optional subject
optional_subject_combobox = ttk.Combobox(root, values=["Optional Math", "Optional Population", "Optional Economics"], font=("Arial", 12))
optional_subject_combobox.grid(row=2, column=1, padx=10, pady=5)
optional_subject_combobox.set("Optional Math")  # Default selection

# Create entry field for optional subject marks
entry_optional = tk.Entry(root, font=("Arial", 12))
entry_optional.grid(row=3, column=1, padx=10, pady=5)  # Moving entry field to below the dropdown

entry_nepali = tk.Entry(root, font=("Arial", 12))
entry_nepali.grid(row=4, column=1, padx=10, pady=5)

entry_english = tk.Entry(root, font=("Arial", 12))
entry_english.grid(row=5, column=1, padx=10, pady=5)

entry_social = tk.Entry(root, font=("Arial", 12))
entry_social.grid(row=6, column=1, padx=10, pady=5)

entry_computer = tk.Entry(root, font=("Arial", 12))
entry_computer.grid(row=7, column=1, padx=10, pady=5)

# Create buttons to increase/decrease marks with arrows
button_math_up = tk.Button(root, text="↑", command=lambda: change_marks(entry_math, 1), font=("Arial", 10))
button_math_up.grid(row=0, column=3, padx=5, pady=5)

button_math_down = tk.Button(root, text="↓", command=lambda: change_marks(entry_math, -1), font=("Arial", 10))
button_math_down.grid(row=0, column=4, padx=5, pady=5)

button_science_up = tk.Button(root, text="↑", command=lambda: change_marks(entry_science, 1), font=("Arial", 10))
button_science_up.grid(row=1, column=3, padx=5, pady=5)

button_science_down = tk.Button(root, text="↓", command=lambda: change_marks(entry_science, -1), font=("Arial", 10))
button_science_down.grid(row=1, column=4, padx=5, pady=5)

# Repeat the same for other subjects
button_optional_up = tk.Button(root, text="↑", command=lambda: change_marks(entry_optional, 1), font=("Arial", 10))
button_optional_up.grid(row=3, column=3, padx=5, pady=5)

button_optional_down = tk.Button(root, text="↓", command=lambda: change_marks(entry_optional, -1), font=("Arial", 10))
button_optional_down.grid(row=3, column=4, padx=5, pady=5)

button_nepali_up = tk.Button(root, text="↑", command=lambda: change_marks(entry_nepali, 1), font=("Arial", 10))
button_nepali_up.grid(row=4, column=3, padx=5, pady=5)

button_nepali_down = tk.Button(root, text="↓", command=lambda: change_marks(entry_nepali, -1), font=("Arial", 10))
button_nepali_down.grid(row=4, column=4, padx=5, pady=5)

button_english_up = tk.Button(root, text="↑", command=lambda: change_marks(entry_english, 1), font=("Arial", 10))
button_english_up.grid(row=5, column=3, padx=5, pady=5)

button_english_down = tk.Button(root, text="↓", command=lambda: change_marks(entry_english, -1), font=("Arial", 10))
button_english_down.grid(row=5, column=4, padx=5, pady=5)

button_social_up = tk.Button(root, text="↑", command=lambda: change_marks(entry_social, 1), font=("Arial", 10))
button_social_up.grid(row=6, column=3, padx=5, pady=5)

button_social_down = tk.Button(root, text="↓", command=lambda: change_marks(entry_social, -1), font=("Arial", 10))
button_social_down.grid(row=6, column=4, padx=5, pady=5)

button_computer_up = tk.Button(root, text="↑", command=lambda: change_marks(entry_computer, 1), font=("Arial", 10))
button_computer_up.grid(row=7, column=3, padx=5, pady=5)

button_computer_down = tk.Button(root, text="↓", command=lambda: change_marks(entry_computer, -1), font=("Arial", 10))
button_computer_down.grid(row=7, column=4, padx=5, pady=5)

# Create a button to calculate the GPA
button_calculate = tk.Button(root, text="Calculate GPA", command=calculate_gpa, font=("Arial", 12), bg="#4CAF50", fg="white")
button_calculate.grid(row=8, column=0, columnspan=5, pady=20)

# Create a label to display the result (GPA, total marks, average)
label_result = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff", fg="green")
label_result.grid(row=9, column=0, columnspan=5, pady=10)

# Run the application
root.mainloop()
