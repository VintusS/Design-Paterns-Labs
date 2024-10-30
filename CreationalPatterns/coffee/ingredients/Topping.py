from enum import Enum


class Topping(Enum):
    CHOCOLATE = "Chocolate"
    CARAMEL = "Caramel"
    VANILLA = "Vanilla"
    HAZELNUT = "Hazelnut"
    CINNAMON = "Cinnamon"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
