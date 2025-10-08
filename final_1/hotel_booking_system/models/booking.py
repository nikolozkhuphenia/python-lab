from datetime import datetime
from final_1.hotel_booking_system.models.customer import Customer
from final_1.hotel_booking_system.models.room import Room


class Booking:

    def __init__(self, customer: Customer, room: Room, total_price: float, status: str, date: datetime):
        self.customer = customer
        self.room = room
        self.total_price = total_price
        self.status = status
        self.date = date

    def __repr__(self):
        return (
            f"<Booking({self.customer.name}, Room {self.room.room_number}, "
            f"${self.total_price}, {self.status} {self.date})>"
        )