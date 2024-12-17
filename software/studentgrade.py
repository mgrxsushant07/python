import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk for ComboBox

# Function to calculate GPA
def calculate_gpa():
    try:
        # Get the marks entered by the user for each subject
        math_marks = int(entry_math.get())
        science_marks = int(entry_science.get())
        optional_marks = int(entry_optional_marks.get())
        nepali_marks = int(entry_nepali.get())
        english_marks = int(entry_english.get())
        social_marks = int(entry_social.get())
        computer_marks = int(entry_computer.get())

        # Check if marks are within valid range (0-100) for all except computer
        if any(marks < 0 or marks > 100 for marks in [math_marks, science_marks, optional_marks, nepali_marks, english_marks, social_marks]):
            messagebox.showerror("Input Error", "Marks should be between 0 and 100 for all subjects except Computer.")
            return
        
        # Check if computer marks are valid (0-50)
        if computer_marks < 0 or computer_marks > 50:
            messagebox.showerror("Input Error", "Computer marks should be between 0 and 50.")
            return

        # Calculate the total marks
        total_marks = (math_marks + science_marks + optional_marks + nepali_marks + english_marks + social_marks + computer_marks)
        
        # Debug print to check total_marks
        print(f"Total Marks: {total_marks}")

        # Calculate GPA (out of 4.0)
        gpa = (total_marks / 650) * 4.0  # Total marks should be out of 750, so this is the correct formula

        # Show the GPA result
        result_label.config(text=f"GPA: {gpa:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Function to save student record
def save_record():
    try:
        math_marks = int(entry_math.get())
        science_marks = int(entry_science.get())
        optional_subject = optional_var.get()
        optional_marks = int(entry_optional_marks.get())
        nepali_marks = int(entry_nepali.get())
        english_marks = int(entry_english.get())
        social_marks = int(entry_social.get())
        computer_marks = int(entry_computer.get())

        # Save the record to a text file
        with open("student_records.txt", "a") as file:
            file.write(f"Mathematics: {math_marks}, Science: {science_marks}, {optional_subject}: {optional_marks}, Nepali: {nepali_marks}, English: {english_marks}, Social: {social_marks}, Computer: {computer_marks}\n")
        
        messagebox.showinfo("Success", "Student record saved successfully!")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Function to update the optional subject marks input
def update_optional_marks():
    selected_subject = optional_var.get()
    
    # Update the label and marks input based on the selected optional subject
    if selected_subject == "Optional Math":
        label_optional_marks.config(text="Optional Math Marks:")
    elif selected_subject == "Optional Population":
        label_optional_marks.config(text="Optional Population Marks:")
    elif selected_subject == "Optional Economics":
        label_optional_marks.config(text="Optional Economics Marks:")
    
    # Clear the current marks input field
    entry_optional_marks.delete(0, tk.END)

# Initialize main window
window = tk.Tk()
window.title("Student Grade Calculator")
window.configure(bg="#e0f7fa")  # Set background color (light cyan)

# Create and pack the labels and spinboxes for each subject
font = ('Helvetica', 12)

label_math = tk.Label(window, text="Mathematics:", font=font, bg="#e0f7fa")
label_math.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_math = tk.Spinbox(window, from_=0, to=100, width=5, font=font)
entry_math.grid(row=0, column=1, padx=10, pady=5)

label_science = tk.Label(window, text="Science:", font=font, bg="#e0f7fa")
label_science.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_science = tk.Spinbox(window, from_=0, to=100, width=5, font=font)
entry_science.grid(row=1, column=1, padx=10, pady=5)

# Dropdown menu for selecting the optional subject (using ttk.Combobox for modern style)
label_optional = tk.Label(window, text="Select Optional Subject:", font=font, bg="#e0f7fa")
label_optional.grid(row=2, column=0, padx=10, pady=5, sticky="w")
optional_subjects = ["Optional Math", "Optional Population", "Optional Economics"]
optional_var = tk.StringVar(window)
optional_var.set(optional_subjects[0])  # Set default to "Optional Math"
entry_optional = ttk.Combobox(window, textvariable=optional_var, values=optional_subjects, state="readonly", width=15, font=font)
entry_optional.grid(row=2, column=1, padx=10, pady=5)

# Update marks entry based on selected optional subject
optional_var.trace("w", lambda *args: update_optional_marks())  # When the value in Combobox changes

# Label for the optional marks (this will change based on the selected subject)
label_optional_marks = tk.Label(window, text="Optional Math Marks:", font=font, bg="#e0f7fa")
label_optional_marks.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_optional_marks = tk.Spinbox(window, from_=0, to=100, width=5, font=font)
entry_optional_marks.grid(row=3, column=1, padx=10, pady=5)

label_nepali = tk.Label(window, text="Nepali:", font=font, bg="#e0f7fa")
label_nepali.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_nepali = tk.Spinbox(window, from_=0, to=100, width=5, font=font)
entry_nepali.grid(row=4, column=1, padx=10, pady=5)

label_english = tk.Label(window, text="English:", font=font, bg="#e0f7fa")
label_english.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_english = tk.Spinbox(window, from_=0, to=100, width=5, font=font)
entry_english.grid(row=5, column=1, padx=10, pady=5)

label_social = tk.Label(window, text="Social Studies:", font=font, bg="#e0f7fa")
label_social.grid(row=6, column=0, padx=10, pady=5, sticky="w")
entry_social = tk.Spinbox(window, from_=0, to=100, width=5, font=font)
entry_social.grid(row=6, column=1, padx=10, pady=5)

label_computer = tk.Label(window, text="Computer:", font=font, bg="#e0f7fa")
label_computer.grid(row=7, column=0, padx=10, pady=5, sticky="w")
entry_computer = tk.Spinbox(window, from_=0, to=50, width=5, font=font)
entry_computer.grid(row=7, column=1, padx=10, pady=5)

# Button to calculate GPA
calculate_button = tk.Button(window, text="Calculate GPA", command=calculate_gpa, font=font, bg="#4CAF50", fg="white", activebackground="#45a049")
calculate_button.grid(row=8, column=0, columnspan=2, pady=10)

# Button to save student record
save_button = tk.Button(window, text="Save Record", command=save_record, font=font, bg="#2196F3", fg="white", activebackground="#1E88E5")
save_button.grid(row=9, column=0, columnspan=2, pady=10)

# Label to display GPA result
result_label = tk.Label(window, text="GPA: ", font=('Helvetica', 14), bg="#e0f7fa", fg="black")
result_label.grid(row=10, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
window.mainloop()
