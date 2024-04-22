import tkinter as tk
from tkinter import messagebox

class BusinessManagementApp:
    def __init__(self, master):
        self.master = master
        master.title("Business Management App")

        self.employee_list = []

        self.label = tk.Label(master, text="Employee Management", font=('Helvetica', 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.age_label = tk.Label(master, text="Age:")
        self.age_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.age_entry = tk.Entry(master)
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_button = tk.Button(master, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(master, text="View Employees", command=self.view_employees)
        self.view_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(master, text="Delete Employee", command=self.delete_employee)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_employee(self):
        name = self.name_entry.get()
        age = self.age_entry.get()

        if name and age:
            self.employee_list.append((name, age))
            messagebox.showinfo("Success", "Employee added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter both name and age.")

    def view_employees(self):
        if self.employee_list:
            employees = "\n".join([f"Name: {emp[0]}, Age: {emp[1]}" for emp in self.employee_list])
            messagebox.showinfo("Employee List", employees)
        else:
            messagebox.showinfo("Employee List", "No employees added yet.")

    def delete_employee(self):
        if self.employee_list:
            name = self.name_entry.get()
            for emp in self.employee_list:
                if emp[0] == name:
                    self.employee_list.remove(emp)
                    messagebox.showinfo("Success", f"Employee {name} deleted successfully!")
                    self.clear_entries()
                    return
            messagebox.showerror("Error", f"Employee {name} not found.")
        else:
            messagebox.showinfo("Employee List", "No employees added yet.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = BusinessManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
