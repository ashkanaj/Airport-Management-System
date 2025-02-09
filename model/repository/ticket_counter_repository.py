from model.entity.ticket_counter import TicketCounter
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

class TicketCounterRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_ticket_counter(self, passenger_id: int, source: str, destination: str, price: float, flight_id: int) -> TicketCounter:
        try:
            new_ticket = TicketCounter(passenger_id=passenger_id, source=source, destination=destination, price=price, flight_id=flight_id)
            self.session.add(new_ticket)
            self.session.commit()
            return new_ticket
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error occurred while creating ticket: {e}")
            return None

    def get_ticket_by_id(self, ticket_id: int) -> TicketCounter:
        try:
            return self.session.query(TicketCounter).filter(TicketCounter.id == ticket_id).first()
        except SQLAlchemyError as e:
            print(f"Error occurred while retrieving ticket by ID: {e}")
            return None

    def get_all_tickets(self) -> list:
        try:
            return self.session.query(TicketCounter).all()
        except SQLAlchemyError as e:
            print(f"Error occurred while retrieving all tickets: {e}")
            return []

    def update_ticket(self, ticket_id: int, source: str, destination: str, price: float, flight_id: int) -> TicketCounter:
        try:
            ticket = self.get_ticket_by_id(ticket_id)
            if ticket:
                ticket.source = source
                ticket.destination = destination
                ticket.price = price
                ticket.flight_id = flight_id
                self.session.commit()
                return ticket
            return None
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error occurred while updating ticket: {e}")
            return None

    def delete_ticket(self, ticket_id: int) -> bool:
        try:
            ticket = self.get_ticket_by_id(ticket_id)
            if ticket:
                self.session.delete(ticket)
                self.session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Error occurred while deleting ticket: {e}")
            return False
