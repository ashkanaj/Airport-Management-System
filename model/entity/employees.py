from sqlalchemy import Column, Integer, String, Float
from model import Base

class Employee(Base):
    __tablename__ = 'employees'

    _employee_id = Column("employee_id", Integer, primary_key=True, autoincrement=True)
    _employee_name = Column("employee_name", String(100), nullable=False)
    _employee_salary = Column("employee_salary", Float, nullable=False)

    def __init__(self, employee_name, employee_salary, employee_id=None):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_salary = employee_salary

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        if isinstance(value, int) and value > 0:
            self._employee_id = value
        else:
            raise ValueError("Employee ID must be a positive integer")

    @property
    def employee_name(self):
        return self._employee_name

    @employee_name.setter
    def employee_name(self, value):
        if isinstance(value, str) and 3 <= len(value) <= 100:
            self._employee_name = value
        else:
            raise ValueError("Employee name must be a string with length between 3 and 100 characters")

    @property
    def employee_salary(self):
        return self._employee_salary

    @employee_salary.setter
    def employee_salary(self, value):
        if isinstance(value, float) and value > 0:
            self._employee_salary = value
        else:
            raise ValueError("Employee salary must be a positive float value")

    def employee_details(self):
        details = (
            f"👤 Employee ID: {self.employee_id}\n"
            f"💼 Employee Name: {self.employee_name}\n"
            f"💵 Salary: ${self.employee_salary}\n"
        )
        return details
