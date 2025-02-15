from model.entity.passengers import Passenger
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class PassengerRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_passenger(self, name: str, age: int, ticket_id: int, luggage_id: int) -> Passenger:
        try:
            new_passenger = Passenger(name=name, age=age, ticket_id=ticket_id, luggage_id=luggage_id)
            self.session.add(new_passenger)
            self.session.commit()
            return new_passenger
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error occurred while creating passenger: {e}")
            return None

    def get_passenger_by_id(self, passenger_id: int) -> Passenger:
        try:
            return self.session.query(Passenger).filter(Passenger.id == passenger_id).first()
        except SQLAlchemyError as e:
            print(f"Error occurred while retrieving passenger by ID: {e}")
            return None

    def get_all_passengers(self) -> list:
        try:
            return self.session.query(Passenger).all()
        except SQLAlchemyError as e:
            print(f"Error occurred while retrieving all passengers: {e}")
            return []

    def update_passenger(self, passenger_id: int, name: str, age: int, ticket_id: int, luggage_id: int) -> Passenger:
        try:
            passenger = self.get_passenger_by_id(passenger_id)
            if passenger:
                passenger.name = name
                passenger.age = age
                passenger.ticket_id = ticket_id
                passenger.luggage_id = luggage_id
                self.session.commit()
                return passenger
            return None
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error occurred while updating passenger: {e}")
            return None

    def delete_passenger(self, passenger_id: int) -> bool:
        try:
            passenger = self.get_passenger_by_id(passenger_id)
            if passenger:
                self.session.delete(passenger)
                self.session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error occurred while deleting passenger: {e}")