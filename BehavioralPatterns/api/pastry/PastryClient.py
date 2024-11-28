from pastry.PastryFactory import PastryFactory
from pastry.enums.PastryType import PastryType


class PastryClient:
    def __init__(self) -> None:
        self._pastry_factory = PastryFactory()

    def make(self, pastry_type: PastryType = None):
        if pastry_type is None:
            print("It is required to specify a pastry type")
        if isinstance(pastry_type, PastryType):
            return self._pastry_factory.create_pastry(pastry_type)
        elif isinstance(pastry_type, str):
            pastry_type = PastryType.from_str(pastry_type)
            return self._pastry_factory.create_pastry(pastry_type)
        else:
            print("Invalid pastry type")
