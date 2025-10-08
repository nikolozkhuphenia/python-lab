import pytest
from final_1.hotel_booking_system.models.customer import Customer
from final_1.hotel_booking_system.models.room import Room

def test_pay_for_booking_success():
    # Arrange
    customer = Customer("Ninja", 1000, [])
    room = Room(101, "standard", 200, True, 2)

    # Act
    result = customer.pay_for_booking(500)

    # Assert
    assert result is True
    assert customer.budget == 500  # 1000 - 500

def test_pay_for_booking_fail():
    # Arrange
    customer = Customer("Ninja", 1000, [])
    room = Room(101, "standard", 200, True, 2)

    # Act
    result = customer.pay_for_booking(500)

    # Assert
    assert result is True
    assert customer.budget == -1  # 1000 - 500