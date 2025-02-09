from model.entity.airport_employees import AirportEmployee
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class AirportEmployeeRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_airport_employee(self, name: str, salary: float, designation: str, department: str) -> AirportEmployee:
        try:
            new_airport_employee = AirportEmployee(name=name, salary=salary, designation=designation, department=department)
            self.session.add(new_airport_employee)
            self.session.commit()
            return new_airport_employee
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error occurred while creating airport employee: {e}")
            return None

    def get_airport_employee_by_id(self, employee_id: int) -> AirportEmployee:
        try:
            return self.session.query(AirportEmployee).filter(AirportEmployee.id == employee_id).first()
        except SQLAlchemyError as e:
            print(f"Error occurred while retrieving airport employee by ID: {e}")
            return None

    def get_all_airport_employees(self) -> list:
        try:
            return self.session.query(AirportEmployee).all()
        except SQLAlchemyError as e:
            print(f"Error occurred while retrieving all airport employees: {e}")
            return []

    def update_airport_employee(self, employee_id: int, name: str, salary: float, designation: str, department: str) -> AirportEmployee:
        try:
            airport_employee = self.get_airport_employee_by_id(employee_id)
            if airport_employee:
                airport_employee.name = name
                airport_employee.salary = salary
                airport_employee.designation = designation
                airport_employee.department = department
                self.session.commit()
                return airport_employee
            return None
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error occurred while updating airport employee: {e}")
            return None

    def delete_airport_employee(self, employee_id: int) -> bool:
        try:
            airport_employee = self.get_airport_employee_by_id(employee_id)
            if airport_employee:
                self.session.delete(airport_employee)
                self.session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error occurred while deleting airport employee: {e}")
            return False
