import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")

        # Task list
        self.tasks = []

        # Frame for task input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.task_input = tk.Entry(self.input_frame, width=30)
        self.task_input.pack(side=tk.LEFT, padx=5)
        self.add_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Frame for task list display
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.list_frame, width=50, height=15)
        self.task_listbox.pack(side=tk.LEFT, padx=5)

        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # Frame for task actions
        self.action_frame = tk.Frame(self.root)
        self.action_frame.pack(pady=10)

        self.remove_button = tk.Button(self.action_frame, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.action_frame, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_input.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.tasks.remove(task)
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "No task selected!")

    def clear_tasks(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
