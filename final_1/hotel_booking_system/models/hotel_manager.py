from final_1.hotel_booking_system.models.customer import Customer
from final_1.hotel_booking_system.models.hotel import Hotel
from final_1.hotel_booking_system.models.room import Room


class HotelManager:
    def __init__(self):
        self.hotels = []
        self.customers = []

    def create_hotel(self, name: str, num_rooms: int) -> Hotel:
        rooms = [
            Room(
                room_number=i + 1,
                room_type="standard" if (i % 2 == 0) else "deluxe",
                price_per_night=500 + (i * 50),
                is_available=True,
                max_guests=2 + (i % 3)
            )
            for i in range(num_rooms)
        ]

        hotel = Hotel(name, rooms, [])
        self.hotels.append(hotel)
        return hotel

    def create_customer(self, name: str, budget: float) -> Customer:
        customer = Customer(name, budget, [])
        self.customers.append(customer)
        return customer

    def list_rooms(self, hotel: Hotel):
        for room in hotel.rooms:
            print(room)