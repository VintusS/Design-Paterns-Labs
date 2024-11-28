from enum import Enum


class MilkType(Enum):
    ALMOND = "Almond"
    REGULAR = "Regular"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
