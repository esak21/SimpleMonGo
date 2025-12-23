from abc import ABC , abstractmethod
from typing import Optional

from domain import Booking, Guest, Room
class IBookingRepository(ABC):

    @abstractmethod
    def add_booking(self, new_booking_data:  Booking):
        raise NotImplementedError


class IRoomRepository(ABC):

    @abstractmethod
    def add_room(self, new_room_data:  Room) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_room_by_id(self, room_id: str) -> Optional[Room]:
        raise NotImplementedError

class IGuestRepository(ABC):

    @abstractmethod
    def get_guest_by_email(self, email: str):
        raise NotImplementedError

    @abstractmethod
    def add_guest(self, new_guest_data:  Guest):
        raise NotImplementedError