import json
from room import Room

class RoomManager:
    def __init__(self):
        self.rooms = []
        self.load_rooms()

    def load_rooms(self):
        with open("rooms.json", "r") as file:
            data = json.load(file)
            for r in data:
                room = Room(r["room_id"], r["room_type"], r["status"], r.get("price", 0))
                self.rooms.append(room)

    def save_rooms(self):
        data = []
        for room in self.rooms:
            data.append({
                "room_id": room.room_id,
                "room_type": room.room_type,
                "status": room.status,
                "price": room.price
            })

        with open("rooms.json", "w") as file:
            json.dump(data, file, indent=4)

    def show_rooms(self):
        print("\nAvailable rooms:")
        for room in self.rooms:
            print(
                f"Room {room.room_id} - {room.room_type} ({room.status}) - ${room.price}"
            )

    def is_room_available(self, room_id):
        for room in self.rooms:
            if room.room_id == room_id:
                if room.status == "available":
                    return True, "Room available"
                elif room.status == "maintenance":
                    return False, "Room under maintenance"
                else:
                    return False, "Room unavailable"

        return False, "Room does not exist"

    def mark_unavailable(self, room_id):
        for room in self.rooms:
            if room.room_id == room_id:
                room.status = "unavailable"
        self.save_rooms()

    def mark_available(self, room_id):
        for room in self.rooms:
            if room.room_id == room_id:
                room.status = "available"
        self.save_rooms()




        
    