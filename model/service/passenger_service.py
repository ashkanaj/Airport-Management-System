from repository.passenger_repository import PassengerRepository
from sqlalchemy.orm import Session

class PassengerService:
    def __init__(self, session: Session):
        self.session = session
        self.repository = PassengerRepository(self.session)

    def create_passenger(self, name: str, age: int, ticket_id: int, luggage_id: int):

        if not name or age < 0:
            return None
        return self.repository.create_passenger(name, age, ticket_id, luggage_id)

    def get_passenger_by_id(self, passenger_id: int):
        return self.repository.get_passenger_by_id(passenger_id)

    def get_all_passengers(self):
        return self.repository.get_all_passengers()

    def update_passenger(self, passenger_id: int, name: str, age: int, ticket_id: int, luggage_id: int):
        if not name or age < 0:
            return None
        return self.repository.update_passenger(passenger_id, name, age, ticket_id, luggage_id)

    def delete_passenger(self, passenger_id: int):
        return self.repository.delete_passenger(passenger_id)
