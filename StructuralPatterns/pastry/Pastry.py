from menu.MenuItem import MenuItem
from .enums.PastryType import PastryType


class Pastry(MenuItem):
    def __init__(self, name: str = None, price: float = None, calories: float = None) -> None:
        super().__init__(name, price)
        self.calories = calories

    def get_calories(self) -> float:
        return self.calories

    def __str__(self) -> str:
        return f"{self.get_name()} - {self.get_price()}, {self.calories} calories"

    def __repr__(self) -> str:
        return self.__str__()

    def show(self) -> str:
        return self.__str__()
