import customtkinter as ctk
from tkinter import messagebox

class ModernTodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("📝 Modern To-Do App")
        self.geometry("500x600")
        ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
        ctk.set_default_color_theme("blue")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="My Tasks", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)

        self.task_var = ctk.StringVar()
        input_frame = ctk.CTkFrame(self, fg_color="transparent")
        input_frame.pack(pady=10)

        self.task_entry = ctk.CTkEntry(input_frame, textvariable=self.task_var, width=300, placeholder_text="Enter new task")
        self.task_entry.pack(side="left", padx=10)

        ctk.CTkButton(input_frame, text="Add", command=self.add_task).pack(side="left")

        self.task_listbox = ctk.CTkTextbox(self, width=400, height=300, font=("Segoe UI", 12), state="disabled")
        self.task_listbox.pack(pady=20)

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10)

        ctk.CTkButton(button_frame, text="Update Task", command=self.update_task).grid(row=0, column=0, padx=5)
        ctk.CTkButton(button_frame, text="Delete Task", command=self.delete_task).grid(row=0, column=1, padx=5)
        ctk.CTkButton(button_frame, text="Clear All", command=self.clear_tasks).grid(row=0, column=2, padx=5)

    def refresh_display(self):
        self.task_listbox.configure(state="normal")
        self.task_listbox.delete("1.0", "end")
        for i, task in enumerate(self.tasks):
            self.task_listbox.insert("end", f"{i+1}. {task}\n")
        self.task_listbox.configure(state="disabled")

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.tasks.append(task)
            self.refresh_display()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def update_task(self):
        index = self.get_selected_index()
        if index is not None:
            new_task = self.task_var.get().strip()
            if new_task:
                self.tasks[index] = new_task
                self.refresh_display()
                self.task_var.set("")
            else:
                messagebox.showwarning("Warning", "Updated task cannot be empty.")
        else:
            messagebox.showinfo("Info", "To update, enter task and select line number in textbox.")

    def delete_task(self):
        index = self.get_selected_index()
        if index is not None:
            del self.tasks[index]
            self.refresh_display()
        else:
            messagebox.showinfo("Info", "Select task number (line) to delete.")

    def clear_tasks(self):
        if messagebox.askyesno("Clear All?", "Are you sure you want to remove all tasks?"):
            self.tasks.clear()
            self.refresh_display()

    def get_selected_index(self):
        try:
            selection = self.task_listbox.get("sel.first linestart", "sel.first lineend")
            index = int(selection.split(".")[0]) - 1
            if 0 <= index < len(self.tasks):
                return index
        except:
            return None


if __name__ == "__main__":
    app = ModernTodoApp()
    app.mainloop()
