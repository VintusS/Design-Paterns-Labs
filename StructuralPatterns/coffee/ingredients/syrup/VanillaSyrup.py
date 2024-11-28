from coffee.ingredients.syrup.Syrup import Syrup


class VanillaSyrup(Syrup):
    def __init__(self) -> None:
        super().__init__()

    def get_flavour(self) -> str:
        return "Vanilla"

    def get_cost(self) -> float:
        return 0.5

    def get_name(self) -> str:
        return "Vanilla Syrup"
