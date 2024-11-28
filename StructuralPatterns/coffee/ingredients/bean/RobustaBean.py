from coffee.ingredients.bean.Bean import Bean


class RobustaBean(Bean):
    def __init__(self) -> None:
        super().__init__()

    def get_origin_country(self) -> str:
        return "Vietnam"

    def get_cost(self) -> float:
        return 0.75

    def get_name(self) -> str:
        return "Robusta Bean"
