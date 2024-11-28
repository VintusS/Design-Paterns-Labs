from coffee.CoffeeIngredient import CoffeeIngredient
from abc import ABC, abstractmethod


class Syrup(CoffeeIngredient, ABC):
    @abstractmethod
    def get_flavour(self) -> str:
        pass
