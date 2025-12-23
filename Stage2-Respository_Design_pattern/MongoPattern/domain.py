from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Room(BaseModel):
    room_number: str
    price_per_night: float
    room_type: str = "suite"
    is_available: bool = True


class Guest(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str


class Booking(BaseModel):
    guest_id: str
    room_id: str
    check_in: datetime
    check_out: datetime
    total_price: float
    status: str = "CONFIRMED"