from model.entity.employees import Employee


class AirportEmployees(Employee):
    def __init__(self,employee_id,employee_name,employee_salary,designation,department):
        super().__init__(employee_id,employee_name,employee_salary)
        self.designation = designation
        self.department = department
        
        
    def employee_details(self):
        parent_details=super().employee_details()


