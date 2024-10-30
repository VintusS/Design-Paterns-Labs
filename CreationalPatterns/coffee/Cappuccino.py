from coffee.enums.CoffeeSize import CoffeeSize
from coffee.enums.DefaultCoffeeType import DefaultCoffeeType
from coffee.CoffeeMenuItem import CoffeeMenuItem
from coffee.ingredients.MilkType import MilkType


class Cappuccino(CoffeeMenuItem):
    def __init__(self):
        super().__init__(name="Cappuccino",
                         price=3.99,
                         type=DefaultCoffeeType.CAPPUCCINO,
                         milk_quantity=100.0,
                         milk_type=MilkType.WHOLE,
                         size=CoffeeSize.MEDIUM)
