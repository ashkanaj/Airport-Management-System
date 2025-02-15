import tkinter as tk
from tkinter import ttk, messagebox
from model.service.airport_employee_service import AirportEmployeeService
import model.service.passenger_service
from model.service.ticket_service import TicketService


employee_service = AirportEmployeeService()
passenger_service = model.service.passenger_service.PassengerService()
ticket_service = TicketService()

class AirportManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Airport Management System")
        self.root.geometry("800x600")

        self.tab_control = ttk.Notebook(root)


        self.employee_tab = ttk.Frame(self.tab_control)
        self.passenger_tab = ttk.Frame(self.tab_control)
        self.ticket_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.employee_tab, text="کارمندان")
        self.tab_control.add(self.passenger_tab, text="مسافران")
        self.tab_control.add(self.ticket_tab, text="بلیط‌ها")

        self.tab_control.pack(expand=1, fill="both")

        self.setup_employee_tab()
        self.setup_passenger_tab()
        self.setup_ticket_tab()


    def setup_employee_tab(self):
        ttk.Label(self.employee_tab, text="نام:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.employee_tab, text="سمت:").grid(row=1, column=0, padx=5, pady=5)

        self.emp_name_entry = ttk.Entry(self.employee_tab)
        self.emp_designation_entry = ttk.Entry(self.employee_tab)

        self.emp_name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.emp_designation_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.employee_tab, text="افزودن کارمند", command=self.add_employee).grid(row=2, column=1, pady=5)

        self.emp_tree = ttk.Treeview(self.employee_tab, columns=("ID", "Name", "Designation"), show="headings")
        self.emp_tree.heading("ID", text="ID")
        self.emp_tree.heading("Name", text="نام")
        self.emp_tree.heading("Designation", text="سمت")
        self.emp_tree.grid(row=3, column=0, columnspan=2, pady=5)

        ttk.Button(self.employee_tab, text="حذف", command=self.delete_employee).grid(row=4, column=1, pady=5)

        self.load_employees()

    def add_employee(self):
        name = self.emp_name_entry.get()
        designation = self.emp_designation_entry.get()
        if name and designation:
            employee_service.add_employee(name, designation)
            self.load_employees()
            self.emp_name_entry.delete(0, tk.END)
            self.emp_designation_entry.delete(0, tk.END)

    def delete_employee(self):
        selected_item = self.emp_tree.selection()
        if selected_item:
            emp_id = self.emp_tree.item(selected_item, "values")[0]
            employee_service.delete_employee(int(emp_id))
            self.load_employees()
        else:
            messagebox.showwarning("هشدار", "لطفاً یک کارمند را انتخاب کنید")

    def load_employees(self):
        for item in self.emp_tree.get_children():
            self.emp_tree.delete(item)
        for emp in employee_service.get_all_employees():
            self.emp_tree.insert("", "end", values=(emp.id, emp.name, emp.designation))

    # -------------------- مسافران -------------------- #
    def setup_passenger_tab(self):
        ttk.Label(self.passenger_tab, text="نام:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.passenger_tab, text="سن:").grid(row=1, column=0, padx=5, pady=5)

        self.pass_name_entry = ttk.Entry(self.passenger_tab)
        self.pass_age_entry = ttk.Entry(self.passenger_tab)

        self.pass_name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.pass_age_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.passenger_tab, text="افزودن مسافر", command=self.add_passenger).grid(row=2, column=1, pady=5)

        self.pass_tree = ttk.Treeview(self.passenger_tab, columns=("ID", "Name", "Age"), show="headings")
        self.pass_tree.heading("ID", text="ID")
        self.pass_tree.heading("Name", text="نام")
        self.pass_tree.heading("Age", text="سن")
        self.pass_tree.grid(row=3, column=0, columnspan=2, pady=5)

        ttk.Button(self.passenger_tab, text="حذف", command=self.delete_passenger).grid(row=4, column=1, pady=5)

        self.load_passengers()

    def add_passenger(self):
        name = self.pass_name_entry.get()
        age = self.pass_age_entry.get()
        if name and age:
            passenger_service.add_passenger(name, int(age))
            self.load_passengers()
            self.pass_name_entry.delete(0, tk.END)
            self.pass_age_entry.delete(0, tk.END)

    def delete_passenger(self):
        selected_item = self.pass_tree.selection()
        if selected_item:
            pass_id = self.pass_tree.item(selected_item, "values")[0]
            passenger_service.delete_passenger(int(pass_id))
            self.load_passengers()
        else:
            messagebox.showwarning("هشدار", "لطفاً یک مسافر را انتخاب کنید")

    def load_passengers(self):
        for item in self.pass_tree.get_children():
            self.pass_tree.delete(item)
        for passenger in passenger_service.get_all_passengers():
            self.pass_tree.insert("", "end", values=(passenger.id, passenger.name, passenger.age))

    # -------------------- بلیط‌ها -------------------- #
    def setup_ticket_tab(self):
        ttk.Label(self.ticket_tab, text="ID مسافر:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.ticket_tab, text="مقصد:").grid(row=1, column=0, padx=5, pady=5)

        self.ticket_passenger_id = ttk.Entry(self.ticket_tab)
        self.ticket_destination = ttk.Entry(self.ticket_tab)

        self.ticket_passenger_id.grid(row=0, column=1, padx=5, pady=5)
        self.ticket_destination.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.ticket_tab, text="افزودن بلیط", command=self.add_ticket).grid(row=2, column=1, pady=5)

    def add_ticket(self):
        passenger_id = self.ticket_passenger_id.get()
        destination = self.ticket_destination.get()
        if passenger_id and destination:
            ticket_service.book_ticket(int(passenger_id), destination)
            messagebox.showinfo("موفق", "بلیط با موفقیت صادر شد")


if __name__ == "__main__":
    root = tk.Tk()
    app = AirportManagementApp(root)
    root.mainloop()
