from abc import ABC, abstractmethod


class CoffeeIngredient(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
