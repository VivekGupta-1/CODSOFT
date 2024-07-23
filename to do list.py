# TO-DO LIST TASK/PROJECT 1 

import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List of TASKS")
        self.tasks = []

        # Create GUI elements
        self.task_number = tk.StringVar()
        self.task_number.set("1 ")

        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack()

        self.delete_button = tk.Button(root, text="Delete task", command=self.delete_task)
        self.delete_button.pack()


    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)


    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(task_index)
            self.tasks.pop(task_index)
        except:
            messagebox.showwarning("ERROR!","Please select a task to delete !")
            
if __name__ == "__main__":

    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()