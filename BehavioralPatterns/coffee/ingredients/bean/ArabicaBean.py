from coffee.ingredients.bean.Bean import Bean


class ArabicaBean(Bean):
    def __init__(self) -> None:
        super().__init__()

    def get_origin_country(self) -> str:
        return "Ethiopia"

    def get_cost(self) -> float:
        return 1.0

    def get_name(self) -> str:
        return "Arabica Bean"
