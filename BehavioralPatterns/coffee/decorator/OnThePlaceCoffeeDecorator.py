from coffee.Coffee import Coffee
from coffee.decorator.CoffeeDecorator import CoffeeDecorator


class OnThePlaceCoffeeDecorator(CoffeeDecorator):
    def __init__(self, coffee: Coffee = None) -> None:
        super().__init__(coffee)
        self.foam_art = "Heart"

    def get_price(self) -> float:
        return super().get_price()

    def get_serving_instructions(self):
        return "On the place"

    def __str__(self) -> str:
        return super().__str__() + " with a foam art of a " + self.foam_art.lower()

    def show(self):
        return self.__str__()

    def mix(self):
        self.foam_art = "Mixed"
        print("Foam art mixed")
