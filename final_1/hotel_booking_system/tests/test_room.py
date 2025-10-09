import pytest
from final_1.hotel_booking_system.models.room import Room

def test_price_calculation():
    room = Room(1, "standard", 600, True, 2)
    assert room.calculate_price(20)

def test_invalid_nights():
    room = Room(1, "standard", 600, True, 2)
    with pytest.raises(ValueError):
     assert room.calculate_price(0)

