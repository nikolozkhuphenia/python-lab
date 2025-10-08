from datetime import datetime
from final_1.hotel_booking_system.models.booking import Booking
from final_1.hotel_booking_system.models.customer import Customer
from final_1.hotel_booking_system.models.room import Room
import logging
logger = logging.getLogger(__name__)

class Hotel:
    logging.basicConfig(filename='logs/booking.log', level=logging.INFO)
    def __init__(self, name: str, rooms : list[Room], bookings_log: list[Booking]):
        self.name = name
        self.rooms = rooms
        self.bookings_log = bookings_log

    def show_available_rooms(self, room_type: str = None) -> list:
        available_rooms = [
            room for room in self.rooms
            if room.is_available and (room_type is None or room.room_type == room_type)
        ]
        return available_rooms

    def calculate_total_booking(self, room_number: int, nights: int) -> float:
         room : Room  = next((r for r in self.rooms if r.room_number == room_number), None) # if/else in for cycle
         if room is not None:
            return room.price_per_night * nights
         else:
             raise ValueError("Room not found!")

    def book_room_for_customer(self, customer: Customer, room_number: int, nights:int) -> bool:

        room: Room = next((r for r in self.rooms if r.room_number == room_number), None)  # if/else in for cycle

        if room is None:
            raise ValueError("Room not found!")
        else:
            if not room.is_available:
               raise ValueError("Room is already booked!")
            else:
                total_price = self.calculate_total_booking(room_number, nights)
                if total_price < 0:
                    raise ValueError("!")
                else:
                    is_booked = customer.pay_for_booking(total_price)
                    if is_booked == False:
                        raise ValueError("Room is already booked!")
                    else:
                        room.book_room()
                        customer.add_room(room)
                        self.log_booking(customer, room, total_price)
                        return True

    def cancel_booking(self, customer: Customer, room_number: int):
        room: Room = next((r for r in customer.booked_rooms if r.room_number == room_number), None)  # if/else in for cycle
        if room is not None:
            room.release_room()
            customer.remove_room(room)
            booking  = self.log_booking_cancel(customer, room_number)
            customer.return_for_booking(booking.total_price)



    def log_booking(self, customer: Customer, room: Room, total_price: float):
        booking = Booking(customer, room, total_price, "Booked", datetime.now())
        self.bookings_log.append(booking)

        # log  in file
        logger.info(f"Room was booked by {customer.name} At: {datetime.now()}")

    def log_booking_cancel(self, customer: Customer, room_number: int) -> Booking :

        for r in self.bookings_log:
            if r.customer == customer and r.room.room_number == room_number:
                r.status = 'Canceled'
                x: Booking = r
                break

        # log  in file
        logger.info(f"Booking was canceled by {customer.name} At: {datetime.now()}")
        return x