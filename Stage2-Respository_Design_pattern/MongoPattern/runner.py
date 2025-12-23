from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
from service import BookingService
from MongoRepository import GuestRepository, RoomsRepository, BookingRepository
from domain import Guest, Room, Booking
from datetime import datetime
from datetime import timedelta

# Load environment variables from .env file
load_dotenv()

uri = os.getenv('MONGO_URI')

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.hotels_db

room_repo =  RoomsRepository(db)
guest_repo = GuestRepository(db)
booking_repo = BookingRepository(db)

service = BookingService(room_repo, guest_repo, booking_repo)

room = Room(room_number="101", price_per_night=100, room_type="Single", is_available=True)

guest_details = Guest(first_name="John", last_name="Doe", email="john.doe@example.com", phone="1234567890")

guest_id = service.create_guest(guest_details)

room_id = service.create_room(room)

no_of_days_staying = 3
checkout = datetime.now() + timedelta(days=no_of_days_staying)

booking_id = service.book_room(guest_id, room_id, datetime.now(), checkout)

print(booking_id)




