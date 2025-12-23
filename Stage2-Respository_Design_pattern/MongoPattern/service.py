from datetime import datetime
from domain import Booking, Guest, Room

class BookingService:
    def __init__(self, room_repo, guest_repo, booking_repo):
        self.room_repo = room_repo
        self.guest_repo = guest_repo
        self.booking_repo = booking_repo

    def create_guest(self, guest: Guest) :
        guest_id = self.guest_repo.add_guest(guest)
        return guest_id

    def create_room(self, room: Room):
        room_id =  self.room_repo.add_room(room)
        return room_id

    def book_room(self, guest_id: str, room_id: str, check_in: datetime, check_out: datetime) :

        room = self.room_repo.get_room_by_id(room_id)
        if not room:
            raise Exception("Room not found")
        if not room.is_available:
            raise Exception("Room is not available")

        nights = (check_out - check_in).days

        total_price = nights * room.price_per_night

        new_booking = Booking(
            guest_id=guest_id,
            room_id= room_id,
            check_in=check_in,
            check_out=check_out,
            total_price=total_price
        )
        booking_id = self.booking_repo.add_booking(new_booking)
        return booking_id
