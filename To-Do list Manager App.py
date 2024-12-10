import tkinter as tk
from tkinter import messagebox


def add_task(task):
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")


def mark_complete():
    try:
        selected_task = task_listbox.curselection()
        task = task_listbox.get(selected_task)
        task_listbox.delete(selected_task)
        task_listbox.insert(tk.END, f"{task} - Done")
    except:
        messagebox.showerror("Error", "Please select a task to mark as complete.")


app = tk.Tk()
app.title("To-Do List Manager")
app.geometry("400x400")


welcome_label = tk.Label(app, text="To-Do List Manager by Ahmad Yasin", font=("Helvetica", 12), fg="pink")
welcome_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))

# Add button and Task entry
task_entry = tk.Entry(app, width=40)
task_entry.grid(row=1, column=0, padx=10, pady=10)

add_button = tk.Button(app, text="Add Task", command=lambda: add_task(task_entry.get()))
add_button.grid(row=1, column=1, padx=10, pady=10)


task_listbox = tk.Listbox(app, width=50, height=15)
task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Complete & Quit Buttons
complete_button = tk.Button(app, text="Mark Complete", command=mark_complete)
complete_button.grid(row=3, column=0, padx=10, pady=10)

quit_button = tk.Button(app, text="Quit", command=app.quit)
quit_button.grid(row=3, column=1, padx=10, pady=10)

# Run 
if __name__ == "__main__":
    app.mainloop()
