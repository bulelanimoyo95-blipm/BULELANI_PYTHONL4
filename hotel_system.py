from room_manager import RoomManager
from booking import Booking
from customer import Customer

class HotelSystem:
    def __init__(self):
        self.room_manager = RoomManager()
        self.bookings = []

    def main_menu(self):
        while True:
            print("\n===== Hotel Booking System =====")
            print("1. Create Booking")
            print("2. View Bookings")
            print("3. Cancel Booking")
            print("4. View Rooms")
            print("5. Exit")

            choice = input("\nEnter your choice (1-5): ")

            if choice == "1":
                self.create_booking()
            elif choice == "2":
                self.view_bookings()
            elif choice == "3":
                self.cancel_booking()
            elif choice == "4":
                self.room_manager.show_rooms()
            elif choice == "5":
                print("Thank you for using our system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_bookings(self):
        if not self.bookings:
            print("\nNo bookings found.")
            return
        
        print("\n===== Bookings =====")
        for booking in self.bookings:
            print(f"Booking ID: {booking.booking_id}")
            print(f"Customer: {booking.customer_name}")
            print(f"Room ID: {booking.room_id}")
            print(f"Check-in: {booking.check_in_date}")
            print(f"Check-out: {booking.check_out_date}")
            print(f"Status: {booking.status}")
            print("-" * 30)

    def create_booking(self):
        self.room_manager.show_rooms()

        name = input("\nEnter your name: ")
        email = input("Enter your email: ")
        room_id = int(input("Enter room ID to book: "))
        check_in = input("Check-in date: ")
        check_out = input("Check-out date: ")

        available, message = self.room_manager.is_room_available(room_id)
        print(message)

        if not available:
            return

        customer = Customer(name, email)
        booking_id = len(self.bookings) + 1
        status = "confirmed"
        booking = Booking(booking_id, customer.name, room_id, check_in, check_out, status)

        self.bookings.append(booking)
        self.room_manager.mark_unavailable(room_id)

        print("Booking confirmed!")

    def cancel_booking(self):
        if not self.bookings:
            print("\nNo bookings to cancel.")
            return
        
        self.view_bookings()
        
        try:
            booking_id = int(input("\nEnter booking ID to cancel: "))
            
            booking_found = False
            for booking in self.bookings:
                if booking.booking_id == booking_id:
                    booking_found = True
                    # Mark room as available again
                    self.room_manager.mark_available(booking.room_id)
                    # Remove the booking
                    self.bookings.remove(booking)
                    print(f"Booking {booking_id} has been cancelled successfully!")
                    print(f"Room {booking.room_id} is now available for booking.")
                    break
            
            if not booking_found:
                print(f"Booking ID {booking_id} not found.")
        except ValueError:
            print("Invalid booking ID. Please enter a number.")

    def make_room_available(self):
        print("Action not permitted: customers cannot change room availability.")

    def end_maintenance(self):
        print("Action not permitted: customers cannot end maintenance for rooms.")
