from coffee.enums.CoffeeSize import CoffeeSize
from coffee.ingredients.Topping import Topping
from coffee.ingredients.CoffeeBeans import CoffeeBeans
from coffee.ingredients.MilkType import MilkType
from coffee.enums.DefaultCoffeeType import DefaultCoffeeType


class Order:
    def __init__(self,
                 coffee_type: DefaultCoffeeType = None,
                 size: CoffeeSize = None,
                 toppings: Topping = None,
                 beans: CoffeeBeans = None,
                 milk: MilkType = None) -> None:
        self.size = size
        self.coffee_type = coffee_type
        self.toppings = toppings
        self.coffee_beans = beans
        self.milk = milk
        self.is_basic = self.coffee_type is not None and self.coffee_beans is None and self.milk is None and self.toppings is None and self.size is None

    def __repr__(self) -> str:
        if self.is_basic:
            return f"Order of a {self.coffee_type}"
        else:
            size = f"{self.size}" if self.size is not None else ""
            toppings = f"{self.toppings}" if self.toppings is not None else ""
            beans = f"{self.coffee_beans}" if self.coffee_beans is not None else ""
            milk = f"{self.milk}" if self.milk is not None else ""
            return f"Order of a {size} {self.coffee_type} with  {beans} beans on {milk} milk and {toppings} on top"
