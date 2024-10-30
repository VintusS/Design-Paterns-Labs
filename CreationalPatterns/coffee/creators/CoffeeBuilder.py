from coffee.CoffeeMenuItem import CoffeeMenuItem
from coffee.ingredients.CoffeeBeans import CoffeeBeans
from coffee.ingredients.MilkType import MilkType
from coffee.ingredients.Topping import Topping
from coffee.enums.DefaultCoffeeType import DefaultCoffeeType
from coffee.enums.CoffeeSize import CoffeeSize
from coffee.Americano import Americano
from coffee.Cappuccino import Cappuccino
from coffee.Latte import Latte
from coffee.Espresso import Espresso


class CoffeeBuilder:
    def __init__(self) -> None:
        self.modifiying_type: CoffeeMenuItem = None
        self.size = None
        self.beans = None
        self.milk = None
        self.toppings = None
        self.milk_quantity = None
        self.price = None
        self.name = None

    def from_type(self, coffee_type: CoffeeMenuItem):
        self.modifiying_type = coffee_type
        self.size = self.modifiying_type.size
        self.beans = self.modifiying_type.beans
        self.milk = self.modifiying_type.milk_type
        self.toppings = self.modifiying_type.toppings
        self.milk_quantity = self.modifiying_type.milk_quantity
        self.name = self.modifiying_type.name
        self.price = self.modifiying_type.price
        return self

    def with_size(self, size: CoffeeSize = None):
        if size is not None and size != self.modifiying_type.size:
            self.size = size
            if self.size == CoffeeSize.SMALL:
                self.milk_quantity = self.modifiying_type.milk_quantity / 2
            elif self.size == CoffeeSize.LARGE:
                self.milk_quantity = self.modifiying_type.milk_quantity * 1.5
                # Increase the price only on large size, you greedy junkie
                self.price = self.modifiying_type.price * 1.2
        return self

    def with_beans(self, beans: CoffeeBeans = None):
        self.beans = beans
        return self

    def with_milk(self, milk: MilkType = None):
        self.milk = milk
        return self

    def with_topping(self, toppings: Topping = None):
        self.toppings = toppings
        return self

    def build(self):
        return CoffeeMenuItem(
            name=self.name,
            price=self.price,
            type=self.modifiying_type.coffee_type,
            size=self.size,
            beans=self.beans,
            milk_type=self.milk,
            milk_quantity=self.milk_quantity,
            toppings=self.toppings,
        )
