from coffee.Coffee import Coffee
from coffee.decorator.CoffeeDecorator import CoffeeDecorator


class TakeOutCoffeeDecorator(CoffeeDecorator):
    def __init__(self, coffee: Coffee = None) -> None:
        super().__init__(coffee)
        self.lid_on = True

    def get_price(self) -> float:
        return super().get_price()

    def show(self):
        return self.__str__()

    def get_serving_instructions(self):
        return "Take out"

    def take_lid_off(self):
        self.lid_on = False
        print("Lid taken off")

    def put_lid_on(self):
        self.lid_on = True
        print("Lid put on")

    def __str__(self) -> str:
        return super().__str__() + " with lid on" if self.lid_on else " with lid off"
