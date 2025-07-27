import tkinter as tk
from tkinter import messagebox, ttk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Modern To-Do App")
        self.root.geometry("500x600")
        self.root.configure(bg="#f4f4f4")

        self.tasks = []

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Segoe UI", 10), padding=6)
        self.style.configure("TEntry", padding=6)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="To-Do List", font=("Segoe UI", 20, "bold"), bg="#f4f4f4", fg="#333").pack(pady=20)

        self.task_var = tk.StringVar()
        entry_frame = tk.Frame(self.root, bg="#f4f4f4")
        entry_frame.pack(pady=10)

        self.task_entry = ttk.Entry(entry_frame, textvariable=self.task_var, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        ttk.Button(entry_frame, text="Add Task", command=self.add_task).pack(side=tk.LEFT)

        self.task_listbox = tk.Listbox(self.root, font=("Segoe UI", 12), width=45, height=15, selectbackground="#a3c9f1")
        self.task_listbox.pack(pady=20)

        button_frame = tk.Frame(self.root, bg="#f4f4f4")
        button_frame.pack()

        ttk.Button(button_frame, text="Update Task", command=self.update_task).grid(row=0, column=0, padx=10)
        ttk.Button(button_frame, text="Delete Task", command=self.delete_task).grid(row=0, column=1, padx=10)
        ttk.Button(button_frame, text="Clear All", command=self.clear_tasks).grid(row=0, column=2, padx=10)

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def update_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            new_task = self.task_var.get().strip()
            if new_task:
                index = selected[0]
                self.tasks[index] = new_task
                self.update_listbox()
                self.task_var.set("")
            else:
                messagebox.showwarning("Warning", "Updated task cannot be empty.")
        else:
            messagebox.showinfo("Info", "Select a task to update.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.update_listbox()
        else:
            messagebox.showinfo("Info", "Select a task to delete.")

    def clear_tasks(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
