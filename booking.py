class Booking:
    def __init__(self, booking_id, customer_name, room_id, check_in_date, check_out_date, status):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = status

    def to_dict(self):
        return {
            "booking_id": self.booking_id,
            "customer_name": self.customer_name,
            "room_id": self.room_id,
            "check_in_date": self.check_in_date,
            "check_out_date": self.check_out_date,
            "status": self.status
        } 