from sqlalchemy import Column, Integer, String, Float
from model.entity.base import Base



class TicketCounter(Base):
    __tablename__ = 'ticket_counters'

    _ticket_id = Column("ticket_id", Integer, primary_key=True, autoincrement=True)
    _passenger_id = Column("passenger_id", Integer, nullable=False)
    _source = Column("source", String(100), nullable=False)
    _destination = Column("destination", String(100), nullable=False)
    _price = Column("price", Float, nullable=False)
    _flight_id = Column("flight_id", Integer, nullable=False)

    def __init__(self, passenger_id, source, destination, price, flight_id, ticket_id=None):
        self.ticket_id = ticket_id
        self.passenger_id = passenger_id
        self.source = source
        self.destination = destination
        self.price = price
        self.flight_id = flight_id

    @property
    def ticket_id(self):
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        if isinstance(value, int) and value > 0:
            self._ticket_id = value
        else:
            raise ValueError("Ticket ID must be a positive integer")

    @property
    def passenger_id(self):
        return self._passenger_id

    @passenger_id.setter
    def passenger_id(self, value):
        if isinstance(value, int) and value > 0:
            self._passenger_id = value
        else:
            raise ValueError("Passenger ID must be a positive integer")

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._source = value
        else:
            raise ValueError("Source must be a non-empty string")

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._destination = value
        else:
            raise ValueError("Destination must be a non-empty string")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, float) and value > 0:
            self._price = value
        else:
            raise ValueError("Price must be a positive float")

    @property
    def flight_id(self):
        return self._flight_id

    @flight_id.setter
    def flight_id(self, value):
        if isinstance(value, int) and value > 0:
            self._flight_id = value
        else:
            raise ValueError("Flight ID must be a positive integer")

    def ticket_details(self):
        details = (
            f"🎟️ Ticket ID: {self.ticket_id}\n"
            f"🛂 Passenger ID: {self.passenger_id}\n"
            f"📍 From: {self.source} -> {self.destination}\n"
            f"💵 Price: ${self.price}\n"
            f"✈️ Flight ID: {self.flight_id}\n"
        )
        return details

    def book_ticket(self):

        if self.price <= 0:
            return "Invalid price. Please enter a valid price."
        else:

            return f"Ticket booked successfully for passenger {self.passenger_id}.\n{self.ticket_details()}"
