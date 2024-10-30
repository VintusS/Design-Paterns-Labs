from coffee.enums.CoffeeSize import CoffeeSize
from coffee.enums.DefaultCoffeeType import DefaultCoffeeType
from coffee.ingredients.MilkType import MilkType
from coffee.ingredients.Topping import Topping
from coffee.ingredients.CoffeeBeans import CoffeeBeans
from menu.MenuItem import MenuItem


class CoffeeMenuItem(MenuItem):
    def __init__(self,
                 name: str = None,
                 price: float = None,
                 type: DefaultCoffeeType = None,
                 beans: CoffeeBeans = CoffeeBeans.ARABICA,
                 toppings: Topping = None,
                 milk_quantity: float = 0.0,
                 milk_type: MilkType = None,
                 size: CoffeeSize = None) -> None:
        super().__init__(name, price)
        self._type = type
        self._beans = beans
        self._milk_quantity = milk_quantity
        self._milk_type = milk_type
        self._size = size
        self._toppings = toppings

    @property
    def toppings(self):
        return self._toppings

    @property
    def milk_type(self):
        return self._milk_type

    @property
    def coffee_type(self):
        return self._type

    @property
    def size(self):
        return self._size

    @property
    def milk_quantity(self):
        return self._milk_quantity

    @property
    def beans(self):
        return self._beans

    def __repr__(self) -> str:
        size = f"{self._size}" if self._size is not None else ""
        toppings = f" and {self._toppings}" if self._toppings is not None else ""
        beans = f"{self._beans}" if self._beans is not None else ""
        milk = f" on {self._milk_type} milk {self._milk_quantity}" if self._milk_type is not None else ""
        return f"{size} {self._type} with {beans} beans{milk}{toppings} - {self._price}"
        # return f"A {self._size} {self._type} with {self._beans} beans, {self._milk_quantity}ml of {self._milk_type} milk and {self._toppings} - {self._price}"
