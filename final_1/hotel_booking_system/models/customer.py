from final_1.hotel_booking_system.models.room import Room

class Customer:
    def __init__(self, name, budget, booked_rooms):
        self.name = name
        self.budget = budget
        self.booked_rooms = booked_rooms
        self.loyalty_points = 0

    def add_room(self, room: Room):
        self.booked_rooms.append(room)

    def remove_room(self, room: Room):
        self.booked_rooms.remove(room)

    def pay_for_booking(self, total_price: float) -> bool:
        if self.budget > total_price:
            self.budget -= total_price
            return True
        else:
            raise ValueError(f"Insufficient balance! Need {total_price} but have {self.budget}")

    def return_for_booking(self, total_price: float) -> None:
        self.budget += total_price

    def show_booking_summary(self):
        for room in self.booked_rooms:
            print(room)

def earn_points(self, total_price: float):
    points = int(total_price / 10)
    self.loyalty_points += points
    return points