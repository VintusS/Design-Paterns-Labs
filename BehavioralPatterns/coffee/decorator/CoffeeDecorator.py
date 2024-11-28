from coffee.Coffee import Coffee


class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee = None) -> None:
        self._wrapped_coffee = coffee
        super().__init__(coffee.get_name(), coffee.get_price())

    def get_price(self) -> float:
        return super().get_price()

    def show(self):
        return self.__str__()

    def __str__(self) -> str:
        return self._wrapped_coffee.show()

    def get_serving_instructions(self):
        return self._wrapped_coffee.get_serving_instructions()
