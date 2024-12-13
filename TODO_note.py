import tkinter as tk
from tkinter import messagebox
import os
import sys

def create_todo_app():
    # Functionality to add a new task
    def add_task():
        task = task_entry.get()
        if task != "":
            tasks_list.insert(tk.END, task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    # Functionality to delete a selected task
    def delete_task():
        try:
            selected_task_index = tasks_list.curselection()[0]
            tasks_list.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    # Functionality to clear all tasks
    def clear_tasks():
        tasks_list.delete(0, tk.END)

    # Functionality to save tasks to a file
    def save_tasks():
        tasks = tasks_list.get(0, tk.END)
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Info", "Tasks saved successfully!")

    # Create main window
    root = tk.Tk()
    root.title("To-Do App")
    root.geometry("400x400")

    # Input field for new tasks
    task_entry = tk.Entry(root, width=40)
    task_entry.pack(pady=10)

    # Buttons
    add_button = tk.Button(root, text="Add Task", command=add_task)
    add_button.pack(pady=5)

    delete_button = tk.Button(root, text="Delete Task", command=delete_task)
    delete_button.pack(pady=5)

    clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
    clear_button.pack(pady=5)

    save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
    save_button.pack(pady=5)

    # Task list display
    tasks_list = tk.Listbox(root, width=50, height=15)
    tasks_list.pack(pady=10)

    # Start the application
    root.mainloop()

# If run as a script, execute the app
if __name__ == "__main__":
    create_todo_app()

# Code for creating a Windows installer
def create_installer():
    try:
        import cx_Freeze

        # Define the target executable
        base = None
        if sys.platform == "win32":
            base = "Win32GUI"

        executables = [cx_Freeze.Executable("todo_app.py", base=base)]

        # Define setup options
        cx_Freeze.setup(
            name="ToDoApp",
            version="1.0",
            description="A simple To-Do application",
            options={
                "build_exe": {
                    "packages": ["tkinter"],
                    "include_files": [],
                }
            },
            executables=executables,
        )

    except ImportError:
        print("Please install cx_Freeze to create the installer.")

# To generate the installer, run:
# python todo_app_installer.py build
