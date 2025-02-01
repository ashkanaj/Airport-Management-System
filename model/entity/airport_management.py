from model.entity.employees import Employee


class AirportManagement(Employee):
    def __init__(self, employee_id, employee_name, employee_salary, designation):
        super().__init__(employee_id, employee_name, employee_salary)
        self.designation = designation

    def employee_details(self):
        parent_details = super().employee_details()

