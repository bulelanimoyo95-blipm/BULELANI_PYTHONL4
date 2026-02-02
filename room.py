class Room:
    def __init__(self, room_id, room_type, status, price=0):
        self.room_id = room_id
        self.room_type = room_type
        self.status = status # 'available', 'booked', 'maintenance'
        self.price = price
        