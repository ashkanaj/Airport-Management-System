from model.entity.employees import Employee
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class EmployeeRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_employee(self, name: str, salary: float) -> Employee:
        try:
            new_employee = Employee(name=name, salary=salary)
            self.session.add(new_employee)
            self.session.commit()
            return new_employee
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error occurred while creating employee: {e}")
            return None

    def get_employee_by_id(self, employee_id: int) -> Employee:
        try:
            return self.session.query(Employee).filter(Employee.id == employee_id).first()
        except SQLAlchemyError as e:
            print(f"Error occurred while retrieving employee by ID: {e}")
            return None

    def get_all_employees(self) -> list:
        try:
            return self.session.query(Employee).all()
        except SQLAlchemyError as e:
            print(f"Error occurred while retrieving all employees: {e}")
            return []

    def update_employee(self, employee_id: int, name: str, salary: float) -> Employee:
        try:
            employee = self.get_employee_by_id(employee_id)
            if employee:
                employee.name = name
                employee.salary = salary
                self.session.commit()
                return employee
            return None
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error occurred while updating employee: {e}")
            return None

    def delete_employee(self, employee_id: int) -> bool:
        try:
            employee = self.get_employee_by_id(employee_id)
            if employee:
                self.session.delete(employee)
                self.session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error occurred while deleting employee: {e}")
            return False
