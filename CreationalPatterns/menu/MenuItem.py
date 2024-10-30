import copy


class MenuItem():
    def __init__(self, name: str = None, price: float = None) -> None:
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def clone(self):
        return copy.deepcopy(self)

    def __repr__(self) -> str:
        return f"{self._name} - {self._price}"
