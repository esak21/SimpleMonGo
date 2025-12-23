from appdomain import Order, OrderModel
from abc import ABC, abstractmethod

class AbstractOrderRepository(ABC):
    @abstractmethod
    def add(self, order: Order):
        raise NotImplementedError

    @abstractmethod
    def get_by_ref(self, order_ref: str ) -> Order | None :
        raise NotImplementedError