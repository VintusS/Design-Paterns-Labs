from coffee.ingredients.milk.Milk import Milk


class RegularMilk(Milk):
    def __init__(self):
        super().__init__()

    def get_cost(self) -> float:
        return 0.5

    def get_name(self) -> str:
        return "Regular Milk"

    def get_type(self) -> str:
        return "Regular Milk"

    def __str__(self) -> str:
        return "Regular Milk"
