from repository.ticket_counter_repository import TicketCounterRepository
from sqlalchemy.orm import Session

class TicketCounterService:
    def __init__(self, session: Session):
        self.session = session
        self.repository = TicketCounterRepository(self.session)

    def create_ticket(self, passenger_id: int, source: str, destination: str, price: float, flight_id: int):

        if price <= 0 or not source or not destination:
            return None
        return self.repository.create_ticket_counter(passenger_id, source, destination, price, flight_id)

    def get_ticket_by_id(self, ticket_id: int):
        return self.repository.get_ticket_by_id(ticket_id)

    def get_all_tickets(self):
        return self.repository.get_all_tickets()

    def update_ticket(self, ticket_id: int, source: str, destination: str, price: float, flight_id: int):
        if price <= 0 or not source or not destination:
            return None
        return self.repository.update_ticket(ticket_id, source, destination, price, flight_id)

    def delete_ticket(self, ticket_id: int):
        return self.repository.delete_ticket(ticket_id)
