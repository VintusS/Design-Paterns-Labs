from coffee.ingredients.milk.Milk import Milk


class AlmondMilk(Milk):
    def __init__(self):
        super().__init__()

    def get_cost(self) -> float:
        return 0.75

    def get_name(self) -> str:
        return "Almond Milk"

    def get_type(self) -> str:
        return "Almond Milk"

    def __str__(self) -> str:
        return "Almond Milk"
