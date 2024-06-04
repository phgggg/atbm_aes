import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class StudentManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        self.students = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.label = tk.Label(self.frame, text="Student Management System", font=('Arial', 16))
        self.label.pack()

        self.add_button = tk.Button(self.frame, text="Add Student", command=self.add_student)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.frame, text="View Students", command=self.view_students)
        self.view_button.pack(pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Student", command=self.delete_student)
        self.delete_button.pack(pady=5)

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

    def add_student(self):
        name = simpledialog.askstring("Input", "Enter student name:")
        if name:
            self.students.append(name)
            self.update_listbox()

    def view_students(self):
        self.update_listbox()
        if not self.students:
            messagebox.showinfo("Info", "No students to display.")

    def delete_student(self):
        selected_student = self.listbox.curselection()
        if selected_student:
            student = self.listbox.get(selected_student)
            self.students.remove(student)
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "No student selected.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for student in self.students:
            self.listbox.insert(tk.END, student)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManager(root)
    root.mainloop()
