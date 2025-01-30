from model import *

class Airline(Base):
    __tablename__ = 'airline'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    airline_name = Column("airline_name",String(30), nullable=False)

    def __init__(self, airline_name):
        self.airline_name = airline_name


