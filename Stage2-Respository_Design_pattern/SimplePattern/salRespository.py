from abstract_product_repository import AbstractOrderRepository
from appdomain import OrderModel, Order


class SQLRepository(AbstractOrderRepository):

    def __init__(self, session ):
        self.session = session

    def add(self, order: Order):
        model = OrderModel(
            order_ref=order.order_ref,
            customer_email=order.customer_email,
            total_amount=order.total_amount,
            status=order.status
        )
        self.session.add(model)


    def get_by_ref(self, order_ref: str ) -> Order | None :
        result_model =  self.session.query(OrderModel).filter_by(order_ref=order_ref).first()
        if not result_model:
            return None
        else:
            return Order(
                order_ref=result_model.order_ref,
                customer_email=result_model.customer_email,
                total_amount=result_model.total_amount,
                status=result_model.status,
                order_id=result_model.order_id
            )
