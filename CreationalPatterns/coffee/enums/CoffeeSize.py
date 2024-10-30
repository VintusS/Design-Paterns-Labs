from enum import Enum


class CoffeeSize(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
