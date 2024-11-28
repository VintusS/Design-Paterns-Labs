from api.coffee.CoffeeClient import CoffeeClient
from api.pastry.PastryClient import PastryClient
from coffee.Coffee import Coffee
from coffee.enums.BeanType import BeanType
from coffee.enums.MilkType import MilkType
from coffee.enums.SyrupType import SyrupType
from order.Order import Order
from pastry.enums.PastryType import PastryType


class OrderClient:
    def __init__(
        self, coffee_client: CoffeeClient, pastry_client: PastryClient
    ) -> None:
        self._coffee_client = coffee_client
        self._pastry_client = pastry_client

    def new(self) -> Order:
        return Order()

    def add_coffee(
        self,
        order: Order = None,
        milk: MilkType = None,
        bean: BeanType = BeanType.ARABICA,
        syrup: SyrupType = None,
        to_go: bool = True,
    ) -> Order:
        if order is None:
            print("It is required to have an order to add a coffee item")
        else:
            coffee = self._coffee_client.make(
                milk=milk, bean=bean, syrup=syrup, take_out=to_go
            )
            order.add(coffee)
            print("Added coffee to order")
            return order

    def add_pastry(self, order: Order = None, pastry_type: PastryType = None) -> Order:
        if order is None:
            print("It is required to have an order to add a pastry item")
        else:
            pastry = self._pastry_client.make(pastry_type)
            order.add(pastry)
            print("Added pastry to order")
            return order
