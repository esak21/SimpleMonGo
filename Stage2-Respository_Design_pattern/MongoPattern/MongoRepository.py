from typing import Optional

import pymongo

from AbstreactRepository import IRoomRepository, IGuestRepository, IBookingRepository
from domain import Guest, Room, Booking
from bson import ObjectId

class GuestRepository(IGuestRepository):
    def __init__(self,db):
        self.collection = db["guest_col"]

    def add_guest(self, new_guest_data: Guest):
        try:
            response = self.collection.insert_one(dict(new_guest_data))
            print(f"A records was inserted into the collection ")
        except Exception:
            raise Exception("Failed to add room")
        return str(response.inserted_id)

    def get_guest_by_email(self, email: str):
        pass

class RoomsRepository(IRoomRepository):
    def __init__(self,db):
        self.collection = db["rooms_col"]

    def add_room(self, new_room_data: Room) -> str:
        try:
            response = self.collection.insert_one(dict(new_room_data))
        except Exception :
            raise Exception("Failed to add room")
        return str(response.inserted_id)

    def get_room_by_id(self, room_id: str) -> Optional[Room]:
        room_id = ObjectId(room_id)
        data = self.collection.find_one({"_id": room_id })
        if not data:
            return None
        return Room(
            room_number=data["room_number"],
            price_per_night=data["price_per_night"],
            room_type=data["room_type"],
            is_available=data["is_available"]
        )


class BookingRepository(IBookingRepository):
    def __init__(self,db):
        self.collection = db["booking_col"]

    def add_booking(self, new_booking_data: Booking) -> str:
        try:
            response = self.collection.insert_one(dict(new_booking_data))
            print(f"A records was inserted into the collection ")
        except Exception :
            raise Exception("Failed to add room")
        return str(response.inserted_id)