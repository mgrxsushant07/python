import tkinter as tk
from tkinter import messagebox, ttk
import csv
from datetime import datetime
 
# File to store the data
FILE_NAME = "visitors.csv"
 
# Create the CSV file if it doesn't exist
def initialize_csv():
    try:
        with open(FILE_NAME, mode="x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Address", "Entry Date & Time"])
    except FileExistsError:
        pass
 
# Function to add entry
def add_entry():
    name = name_var.get()
    phone = phone_var.get()
    address = address_var.get()
    if not name or not phone or not address:
        messagebox.showerror("Input Error", "All fields are required!")
        return
 
    entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, address, entry_time])
    messagebox.showinfo("Success", "Entry added successfully!")
 
    # Clear the input fields
    name_var.set("")
    phone_var.set("")
    address_var.set("")
 
    # Automatically retrieve and display updated entries
    view_entries()
 
# Function to delete selected entry
def delete_entry():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror("Error", "No entry selected!")
        return
 
    data = tree.item(selected_item, "values")
    all_entries = []
 
    # Read existing entries
    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        all_entries = list(reader)
 
    # Remove the selected entry
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for entry in all_entries:
            if entry != list(data):
                writer.writerow(entry)
 
    messagebox.showinfo("Success", "Entry deleted successfully!")
 
    # Automatically refresh the table
    view_entries()
 
# Function to view all entries
def view_entries():
    for row in tree.get_children():
        tree.delete(row)
 
    try:
        with open(FILE_NAME, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                tree.insert("", "end", values=row)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found!")
 
# Initialize the CSV file
initialize_csv()
 
# GUI setup
root = tk.Tk()
root.title("Visitor Entry System")
root.geometry("900x600")
root.configure(bg="#1E1E2F")  # Translucent-like futuristic background
root.attributes('-alpha', 0.95)  # Set transparency
 
# Fonts and styles
font_title = ("Arial", 16, "bold")
font_label = ("Arial", 12)
font_button = ("Arial", 10, "bold")
 
# Variables
name_var = tk.StringVar()
phone_var = tk.StringVar()
address_var = tk.StringVar()
 
# Input fields
frame = tk.Frame(root, bg="#2B2B3C", bd=5, relief="groove")
frame.pack(pady=10, padx=10, fill=tk.X)
 
tk.Label(frame, text="Name:", font=font_label, fg="white", bg="#2B2B3C").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(frame, textvariable=name_var, font=font_label, width=25).grid(row=0, column=1, padx=10, pady=10)
 
tk.Label(frame, text="Phone:", font=font_label, fg="white", bg="#2B2B3C").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(frame, textvariable=phone_var, font=font_label, width=25).grid(row=1, column=1, padx=10, pady=10)
 
tk.Label(frame, text="Address:", font=font_label, fg="white", bg="#2B2B3C").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(frame, textvariable=address_var, font=font_label, width=25).grid(row=2, column=1, padx=10, pady=10)
 
# Buttons
tk.Button(frame, text="Add Entry", command=add_entry, font=font_button, bg="#4CAF50", fg="white", bd=3).grid(row=3, column=0, padx=10, pady=10)
tk.Button(frame, text="Delete Entry", command=delete_entry, font=font_button, bg="#F44336", fg="white", bd=3).grid(row=3, column=1, padx=10, pady=10)
 
# Treeview for displaying entries
style = ttk.Style()
style.configure("Treeview", font=("Arial", 10), rowheight=25, fieldbackground="#1E1E2F", background="#1E1E2F", foreground="white")
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#33334C", foreground="white")
style.map("Treeview", background=[("selected", "#4CAF50")])
 
frame_table = tk.Frame(root, bg="#2B2B3C", bd=5, relief="groove")
frame_table.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
 
tree = ttk.Treeview(frame_table, columns=("Name", "Phone", "Address", "Entry Date & Time"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Address", text="Address")
tree.heading("Entry Date & Time", text="Entry Date & Time")
 
tree.pack(fill=tk.BOTH, expand=True)
 
# Scrollbar
scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
 
# View Entries initially
view_entries()
 
root.mainloop()