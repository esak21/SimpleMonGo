from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, MappedAsDataclass
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dataclasses import dataclass




@dataclass
class Order:
    order_ref: str
    customer_email: str
    total_amount: float
    status: str = "PENDING"
    order_id: int = None





class Base(MappedAsDataclass, DeclarativeBase):
    pass

class OrderModel(Base):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(primary_key=True, init=False)
    order_ref: Mapped[str] = mapped_column(String(50), unique=True)
    customer_email: Mapped[str] = mapped_column(String(100))
    total_amount: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(default="PENDING")