import tkinter as tk
from tkinter import messagebox

# Class 1
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa


# Class 2
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, gpa):
        student = Student(name, gpa)
        self.students.append(student)

    def get_students(self):
        return self.students

    def update_student(self, name, new_gpa):
        for student in self.students:
            if student.name == name:
                student.gpa = new_gpa
                return True
        return False

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return True
        return False


# Class 3
class StudentGUI:
    def __init__(self, root):
        self.manager = StudentManager()
        self.root = root
        self.root.title("Student Records Management System")
        self.root.geometry("400x400")

        tk.Label(root, text="Student Records System", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(root, text="Name").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="GPA").pack()
        self.gpa_entry = tk.Entry(root)
        self.gpa_entry.pack()

        tk.Button(root, text="Add Student", command=self.add_student).pack(pady=5)
        tk.Button(root, text="Update Student", command=self.update_student).pack(pady=5)
        tk.Button(root, text="Delete Student", command=self.delete_student).pack(pady=5)
        tk.Button(root, text="Show Students", command=self.show_students).pack(pady=5)
        tk.Button(root, text="Clear", command=self.clear_fields).pack(pady=5)

        self.output = tk.Text(root, height=10, width=45)
        self.output.pack(pady=10)

    def add_student(self):
        name = self.name_entry.get()
        gpa_text = self.gpa_entry.get()

        if name == "" or gpa_text == "":
            messagebox.showerror("Error", "Please enter name and GPA")
            return

        try:
            gpa = float(gpa_text)
        except:
            messagebox.showerror("Error", "GPA must be a number")
            return

        self.manager.add_student(name, gpa)
        messagebox.showinfo("Success", "Student added")
        self.clear_fields()

    def update_student(self):
        name = self.name_entry.get()
        gpa_text = self.gpa_entry.get()

        if name == "" or gpa_text == "":
            messagebox.showerror("Error", "Please enter name and new GPA")
            return

        try:
            gpa = float(gpa_text)
        except:
            messagebox.showerror("Error", "GPA must be a number")
            return

        if self.manager.update_student(name, gpa):
            messagebox.showinfo("Success", "Student updated")
        else:
            messagebox.showerror("Error", "Student not found")

        self.clear_fields()

    def delete_student(self):
        name = self.name_entry.get()

        if name == "":
            messagebox.showerror("Error", "Please enter a name")
            return

        if self.manager.delete_student(name):
            messagebox.showinfo("Success", "Student deleted")
        else:
            messagebox.showerror("Error", "Student not found")

        self.clear_fields()

    def show_students(self):
        self.output.delete("1.0", tk.END)

        students = self.manager.get_students()

        if len(students) == 0:
            self.output.insert(tk.END, "No student records found.\n")
            return

        for student in students:
            text = "Name: " + student.name + " | GPA: " + str(student.gpa)

            if student.gpa >= 3.5:
                text = text + " | Honors"

            self.output.insert(tk.END, text + "\n")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.gpa_entry.delete(0, tk.END)


root = tk.Tk()
app = StudentGUI(root)
root.mainloop()