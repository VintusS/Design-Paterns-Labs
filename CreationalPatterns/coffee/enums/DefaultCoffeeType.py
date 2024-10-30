from enum import Enum


class DefaultCoffeeType(Enum):
    ESPRESSO = "Espresso"
    LATTE = "Latte"
    CAPPUCCINO = "Cappuccino"
    AMERICANO = "Americano"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
