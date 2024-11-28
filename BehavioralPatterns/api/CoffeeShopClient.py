from api.coffee.CoffeeClient import CoffeeClient
from api.order.OrderClient import OrderClient
from api.pastry.PastryClient import PastryClient
from coffee.creators.builder.CoffeeBuilder import CoffeeBuilder
from employee.barista.Barista import Barista
from order.builder.OrderBuilder import OrderBuilder
from pastry.PastryFactory import PastryFactory


class CoffeeShopClient:
    def __init__(self) -> None:
        self._barista = Barista(name="John")
        self.coffee = CoffeeClient(barista=self._barista)
        self.pastry = PastryClient()
        self.orders = OrderClient(coffee_client=self.coffee, pastry_client=self.pastry)
