from sqlalchemy import Column, Integer, String
from model.entity.base import Base



class Passenger(Base):
    __tablename__ = 'passengers'

    _passenger_id = Column("passenger_id", Integer, primary_key=True, autoincrement=True)
    _passenger_name = Column("passenger_name", String(100), nullable=False)
    _passenger_age = Column("passenger_age", Integer, nullable=False)
    _ticket_id = Column("ticket_id", Integer, nullable=False)
    _luggage_id = Column("luggage_id", Integer, nullable=False)
    _is_checked_in = Column("is_checked_in", Boolean, default=False)

    def __init__(self, passenger_name, passenger_age, ticket_id, luggage_id, passenger_id=None):
        self.passenger_id = passenger_id
        self.passenger_name = passenger_name
        self.passenger_age = passenger_age
        self.ticket_id = ticket_id
        self.luggage_id = luggage_id

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
    def passenger_name(self):
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._passenger_name = value
        else:
            raise ValueError("Passenger name must be a non-empty string")

    @property
    def passenger_age(self):
        return self._passenger_age

    @passenger_age.setter
    def passenger_age(self, value):
        if isinstance(value, int) and value > 0:
            self._passenger_age = value
        else:
            raise ValueError("Passenger age must be a positive integer")

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
    def luggage_id(self):
        return self._luggage_id

    @luggage_id.setter
    def luggage_id(self, value):
        if isinstance(value, int) and value > 0:
            self._luggage_id = value
        else:
            raise ValueError("Luggage ID must be a positive integer")

    @property
    def is_checked_in(self):
        return self._is_checked_in

    @is_checked_in.setter
    def is_checked_in(self, value):
        self._is_checked_in = bool(value)

    def passenger_details(self):
        details = (
            f"🛂 Passenger ID: {self.passenger_id}\n"
            f"👤 Name: {self.passenger_name}\n"
            f"🎂 Age: {self.passenger_age}\n"
            f"🎟️ Ticket ID: {self.ticket_id}\n"
            f"🧳 Luggage ID: {self.luggage_id}\n"
            f"✅ Checked In: {'Yes' if self.is_checked_in else 'No'}\n"
        )
        return details

    def check_in(self):
        if not self.is_checked_in:
            self.is_checked_in = True
            return f"{self.passenger_name} has successfully checked in."
        else:
            return f"{self.passenger_name} is already checked in."
