from coffee.CoffeeIngredient import CoffeeIngredient
from abc import ABC, abstractmethod


class Milk(CoffeeIngredient):
    @abstractmethod
    def get_type(self) -> str:
        pass
