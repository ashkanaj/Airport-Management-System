from model.entity.employees import Employee


class AirportEmployees(Employee):
    def __init__(self, employee_id, employee_name, employee_salary, designation, department):

        super().__init__(employee_name=employee_name, employee_salary=employee_salary, employee_id=employee_id)
        self.designation = designation
        self.department = department

    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._designation = value
        else:
            raise ValueError("Designation must be a non-empty string")

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._department = value
        else:
            raise ValueError("Department must be a non-empty string")

    def employee_details(self):

        parent_details = super().employee_details()


        additional_details = (
            f"🧳 Designation: {self.designation}\n"
            f"🏢 Department: {self.department}\n"
        )


        return parent_details + additional_details
