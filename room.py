class Room:
    def __init__(self, room_id, room_type, status, price=0):
        self.room_id = room_id
        self.room_type = room_type
        self.status = status # 'available', 'booked', 'maintenance'
        self.price = price

    def amenities(self):
        return "Basic amenities"

    def display_line(self):
        return (
            f"Room {self.room_id} - {self.room_type} ({self.status}) - ${self.price}"
            f" | {self.amenities()}"
        )


class SingleRoom(Room):
    def amenities(self):
        return "Single bed, Wi-Fi"


class DoubleRoom(Room):
    def amenities(self):
        return "Double bed, Wi-Fi, TV"


class SuiteRoom(Room):
    def amenities(self):
        return "King bed, living area, Wi-Fi, TV, minibar"
        