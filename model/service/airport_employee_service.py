from sqlalchemy.orm import Session


class AirportEmployeeService:
    def __init__(self, session: Session):
        self.session = session
        self.repository = AirportEmployeeRepository(self.session)

    def create_airport_employee(self, name: str, salary: float, designation: str, department: str):

        if not name or salary <= 0:
            return None
        return self.repository.create_airport_employee(name, salary, designation, department)

    def get_airport_employee_by_id(self, employee_id: int):
        return self.repository.get_airport_employee_by_id(employee_id)

    def get_all_airport_employees(self):
        return self.repository.get_all_airport_employees()

    def update_airport_employee(self, employee_id: int, name: str, salary: float, designation: str, department: str):

        if not name or salary <= 0:
            return None
        return self.repository.update_airport_employee(employee_id, name, salary, designation, department)

    def delete_airport_employee(self, employee_id: int):
        return self.repository.delete_airport_employee(employee_id)
