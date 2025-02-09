class Flight:
    def __init__(self, flight_id, flight_name, capacity, starting_time, reaching_time, source, destination, price):
        self.flight_id = flight_id
        self.flight_name = flight_name
        self.capacity = capacity
        self.available_seats = capacity
        self.starting_time = starting_time
        self.reaching_time = reaching_time
        self.source = source
        self.destination = destination
        self.price = price
        self.status = "Scheduled"
        self.pilot = None

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
