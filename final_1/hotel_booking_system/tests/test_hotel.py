import pytest
from final_1.hotel_booking_system.models.hotel import Hotel
from final_1.hotel_booking_system.models.room import Room


def test_show_available_rooms():
    hotel = Hotel("Test_Hotel", [1,2],[1])
    room = Room(1, "standard", 600, True, 2)
    assert room.room_type == "deluxe"