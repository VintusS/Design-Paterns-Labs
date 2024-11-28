from pastry.Pastry import Pastry


class PainAuChocolat(Pastry):
    def __init__(
        self, name: str = "Pain au chocolat", price: float = 3.5, calories: float = 300
    ) -> None:
        super().__init__(name, price, calories)

    def __str__(self) -> str:
        return f"{self.get_name()} - {self.get_price()}, {self.get_calories()} calories"

    def __repr__(self) -> str:
        return self.__str__()

    def show(self) -> str:
        return self.__str__()
