from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from salRespository import SQLRepository
from appdomain import Order, Base

# 1. Initialize Database
engine = create_engine("sqlite:///orders_only.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# 2. Use the Repository in a business flow
with Session() as session:
    repo = SQLRepository(session)

    # Creating a domain object
    new_order = Order(order_ref="ORD-1003", customer_email="user@example.com", total_amount=45.99)

    # Adding via repo
    repo.add(new_order)

    # Commit the session (Unit of Work responsibility)
    session.commit()

    # Retrieving
    retrieved = repo.get_by_ref("ORD-1000")
    print(f"Retrieved Order: {retrieved.order_ref} - Status: {retrieved}")