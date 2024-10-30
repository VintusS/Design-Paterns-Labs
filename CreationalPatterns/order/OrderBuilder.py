from order.Order import Order


class OrderBuilder:
    def __init__(self):
        self.coffee_type = None
        self.size = None
        self.toppings = None
        self.beans = None
        self.milk = None

    def of_type(self, coffee_type):
        self.coffee_type = coffee_type
        return self

    def with_size(self, size):
        self.size = size
        return self

    def with_beans(self, beans):
        self.beans = beans
        return self

    def with_milk(self, milk):
        self.milk = milk
        return self

    def with_topping(self, topping):
        self.toppings = topping
        return self

    def build(self):
        if self.coffee_type is None:
            raise ValueError(
                "Cannot brew coffee without specifying a base type of it.")
        return Order(
            coffee_type=self.coffee_type,
            size=self.size,
            toppings=self.toppings,
            beans=self.beans,
            milk=self.milk
        )
