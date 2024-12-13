import csv
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

def save_entry(name, phone, address, tree):
    """
    Saves an entry with name, phone, address, and current datetime to a CSV file and updates the treeview.
    """
    entry_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("entries.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, address, entry_datetime])
    tree.insert("", tk.END, values=(name, phone, address, entry_datetime))
    messagebox.showinfo("Success", "Entry saved successfully.")

def retrieve_entries(tree):
    """
    Retrieves all entries from the CSV file and populates the treeview.
    """
    try:
        with open("entries.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in tree.get_children():
                tree.delete(row)
            for row in reader:
                tree.insert("", tk.END, values=row)
    except FileNotFoundError:
        messagebox.showwarning("Error", "No entries found. The file does not exist.")

def search_entries(search_term, tree):
    """
    Searches for entries in the CSV file containing the search term and displays them in the treeview.
    """
    try:
        with open("entries.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in tree.get_children():
                tree.delete(row)
            for row in reader:
                if any(search_term.lower() in field.lower() for field in row):
                    tree.insert("", tk.END, values=row)
    except FileNotFoundError:
        messagebox.showwarning("Error", "No entries found. The file does not exist.")

def main():
    root = tk.Tk()
    root.title("Technology Channel Entry System")

    # Frame for input fields
    input_frame = ttk.Frame(root, padding="10")
    input_frame.grid(row=0, column=0, sticky="ew")

    ttk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="w")
    name_entry = ttk.Entry(input_frame, width=30)
    name_entry.grid(row=0, column=1, sticky="w")

    ttk.Label(input_frame, text="Phone:").grid(row=1, column=0, sticky="w")
    phone_entry = ttk.Entry(input_frame, width=30)
    phone_entry.grid(row=1, column=1, sticky="w")

    ttk.Label(input_frame, text="Address:").grid(row=2, column=0, sticky="w")
    address_entry = ttk.Entry(input_frame, width=30)
    address_entry.grid(row=2, column=1, sticky="w")

    # Frame for treeview
    tree_frame = ttk.Frame(root, padding="10")
    tree_frame.grid(row=1, column=0, sticky="nsew")

    columns = ("Name", "Phone", "Address", "Entry Datetime")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    tree.pack(fill="both", expand=True)

    retrieve_button = ttk.Button(root, text="Retrieve Entries", command=lambda: retrieve_entries(tree))
    retrieve_button.grid(row=2, column=0, pady=10)

    # Search functionality
    search_frame = ttk.Frame(root, padding="10")
    search_frame.grid(row=3, column=0, sticky="ew")

    ttk.Label(search_frame, text="Search:").grid(row=0, column=0, sticky="w")
    search_entry = ttk.Entry(search_frame, width=30)
    search_entry.grid(row=0, column=1, sticky="w")

    search_button = ttk.Button(search_frame, text="Search", command=lambda: search_entries(search_entry.get(), tree))
    search_button.grid(row=0, column=2, padx=5)

    def save_action():
        name = name_entry.get()
        phone = phone_entry.get()
        address = address_entry.get()
        if name and phone and address:
            save_entry(name, phone, address, tree)
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    save_button = ttk.Button(input_frame, text="Save Entry", command=save_action)
    save_button.grid(row=3, column=0, columnspan=2, pady=10)

    retrieve_entries(tree)
    root.mainloop()

if __name__ == "__main__":
    main()