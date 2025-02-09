from datetime import datetime, date
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from model.entity.base import Base



class Flight(Base):
    __tablename__ = 'flights'

    _flight_id = Column("flight_id", Integer, primary_key=True, autoincrement=True)
    _flight_name = Column("flight_name", String(100), nullable=False)
    _capacity = Column("capacity", Integer, nullable=False)
    _available_seats = Column("available_seats", Integer, nullable=False)
    _starting_time = Column("starting_time", DateTime, nullable=False)
    _reaching_time = Column("reaching_time", DateTime, nullable=False)
    _source = Column("source", String(50), nullable=False)
    _destination = Column("destination", String(50), nullable=False)
    _price = Column("price", Float, nullable=False)
    _status = Column("status", String(50), default="Scheduled")
    _pilot = Column("pilot", String(100), nullable=True)

    def __init__(self, flight_name, capacity, starting_time, reaching_time, source, destination, price,
                 status="Scheduled", pilot=None, flight_id=None):
        self.flight_id = flight_id
        self.flight_name = flight_name
        self.capacity = capacity
        self.available_seats = capacity  # Initially, available seats = capacity
        self.starting_time = starting_time
        self.reaching_time = reaching_time
        self.source = source
        self.destination = destination
        self.price = price
        self.status = status
        self.pilot = pilot

    @property
    def flight_id(self):
        return self._flight_id

    @flight_id.setter
    def flight_id(self, value):
        self._flight_id = value

    @property
    def flight_name(self):
        return self._flight_name

    @flight_name.setter
    def flight_name(self, value):
        if isinstance(value, str) and 3 <= len(value) <= 100:
            self._flight_name = value
        else:
            raise ValueError("Flight name must be a string with length between 3 and 100 characters")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if isinstance(value, int) and value > 0:
            self._capacity = value
            self._available_seats = value  # Update available seats based on capacity
        else:
            raise ValueError("Capacity must be a positive integer")

    @property
    def available_seats(self):
        return self._available_seats

    @available_seats.setter
    def available_seats(self, value):
        if 0 <= value <= self._capacity:
            self._available_seats = value
        else:
            raise ValueError("Available seats must be between 0 and capacity")

    @property
    def starting_time(self):
        return self._starting_time

    @starting_time.setter
    def starting_time(self, value):
        if isinstance(value, datetime):
            self._starting_time = value
        else:
            raise ValueError("Starting time must be a valid datetime object")

    @property
    def reaching_time(self):
        return self._reaching_time

    @reaching_time.setter
    def reaching_time(self, value):
        if isinstance(value, datetime):
            self._reaching_time = value
        else:
            raise ValueError("Reaching time must be a valid datetime object")

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
            raise ValueError("Price must be a positive float value")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value in ["Scheduled", "Completed", "Cancelled"]:
            self._status = value
        else:
            raise ValueError("Status must be one of: 'Scheduled', 'Completed', 'Cancelled'")

    @property
    def pilot(self):
        return self._pilot

    @pilot.setter
    def pilot(self, value):
        if value is None or isinstance(value, str):
            self._pilot = value
        else:
            raise ValueError("Pilot must be a string or None")

    def flight_details(self):
        details = (
            f"✈️ Flight ID: {self.flight_id}\n"
            f"📍 Flight Name: {self.flight_name}\n"
            f"🛫 From: {self.source} -> 🛬 To: {self.destination}\n"
            f"⏰ Time: {self.starting_time} - {self.reaching_time}\n"
            f"🎟️ Price: {self.price} USD\n"
            f"🧑‍✈️ Pilot: {self.pilot if self.pilot else 'Not Assigned'}\n"
            f"🪑 Seats Available: {self.available_seats}/{self.capacity}\n"
            f"📌 Status: {self.status}"
        )
        return details
