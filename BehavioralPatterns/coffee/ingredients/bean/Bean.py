from abc import ABC, abstractmethod
from coffee.CoffeeIngredient import CoffeeIngredient


class Bean(CoffeeIngredient, ABC):
    @abstractmethod
    def get_origin_country(self) -> str:
        pass
