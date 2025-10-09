
from final_1.hotel_booking_system.models.hotel_manager import HotelManager
import logging
logger = logging.getLogger(__name__)

manager = HotelManager()

hotel1 = manager.create_hotel("Python Hotel", 100)

customer1 = manager.create_customer("Ninja", 25000)
customer2 = manager.create_customer("Jinja", 15000)

#manager.list_rooms(hotel1)


try:
    hotel1.book_room_for_customer(customer1, 1, 5)
    hotel1.book_room_for_customer(customer1, 2, 4)
    hotel1.cancel_booking(customer1, 1)
    hotel1.book_room_for_customer(customer1, 7, 5)


    for user1 in hotel1.bookings_log:
        print(user1)

    print(customer1.budget)

except ValueError as e:
    logger.error(f"Error occurred: {e}")
    print('Room booking failed')

