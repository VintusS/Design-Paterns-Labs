class MenuItem():
    def __init__(self, name: str = None, price: float = None) -> None:
        self._name = name
        self._price = price

    def show(self):
        return self._name

    def get_price(self):
        return self._price

    def get_name(self):
        return self._name

    def __repr__(self) -> str:
        return f"{self._name} - {self._price}"
