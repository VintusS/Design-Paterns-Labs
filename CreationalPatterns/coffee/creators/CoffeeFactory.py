from menu.Menu import Menu
from order.Order import Order
from coffee.creators.CoffeeBuilder import CoffeeBuilder


class CoffeeFactory:
    def __init__(self):
        menu = Menu.get_instance()
        menu_items = menu.get_menu_items()
        self._coffee_types = {}
        for item in menu_items:
            item_coffee_type = item.coffee_type.value
            item_prototype = item
            self._coffee_types[item_coffee_type] = item_prototype

    def create_coffee(self, order: Order):
        if order.is_basic:
            return self._coffee_types[order.coffee_type.value].clone()
        else:
            coffee_builder = CoffeeBuilder()
            coffee_builder.from_type(
                self._coffee_types[order.coffee_type.value])
            coffee_builder.with_size(order.size)
            coffee_builder.with_beans(order.coffee_beans)
            coffee_builder.with_milk(order.milk)
            coffee_builder.with_topping(order.toppings)
            return coffee_builder.build()
