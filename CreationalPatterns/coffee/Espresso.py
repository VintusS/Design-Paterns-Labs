from coffee.enums.CoffeeSize import CoffeeSize
from coffee.enums.DefaultCoffeeType import DefaultCoffeeType
from coffee.CoffeeMenuItem import CoffeeMenuItem


class Espresso(CoffeeMenuItem):
    def __init__(self):
        super().__init__(name="Espresso",
                         price=1.99,
                         type=DefaultCoffeeType.ESPRESSO,
                         size=CoffeeSize.SMALL)
