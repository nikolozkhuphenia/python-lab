class Room:

    def __init__(self,
        room_number: int,
        room_type: str,
        price_per_night: float,
        is_available: bool,
        max_guests: int):

        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = is_available
        self.max_guests = max_guests

    def book_room(self):
        self.is_available = False

    def release_room(self):
        self.is_available = True

    def calculate_price(self, nights: int) -> float:
        if not isinstance(nights, int):
            raise TypeError("Number of nights must be an integer")
        if nights <= 0:
            raise ValueError("Number of nights must be greater than 0")

        return self.price_per_night * nights

    def __str__(self):
        status = "Available" if self.is_available else "Booked"
        return f"Room #{self.room_number} | {self.room_type} | {self.price_per_night}/night | {status} | Max: {self.max_guests} guests"