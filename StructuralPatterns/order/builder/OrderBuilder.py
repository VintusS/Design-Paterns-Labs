from coffee.Coffee import Coffee
from order.Order import Order
from pastry.Pastry import Pastry


class OrderBuilder():
    def __init__(self) -> None:
        self.order_items = []

    def add_coffee(self, coffee: Coffee):
        self.order_items.append(coffee)
        return self

    def add_pastry(self, pastry: Pastry):
        self.order_items.append(pastry)
        return self

    def add_item(self, item):
        self.order_items.append(item)
        return self

    def build(self):
        return Order(self.order_items)
