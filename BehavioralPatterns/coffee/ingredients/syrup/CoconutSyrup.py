from coffee.ingredients.syrup.Syrup import Syrup


class CoconutSyrup(Syrup):
    def get_flavour(self) -> str:
        return "Coconut"

    def get_cost(self) -> float:
        return 0.5

    def get_name(self) -> str:
        return "Coconut Syrup"
