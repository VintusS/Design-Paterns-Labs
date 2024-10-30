from enum import Enum


class MilkType(Enum):
    WHOLE = "Whole"
    SEMI_SKIMMED = "Semi-Skimmed"
    SKIMMED = "Skimmed"
    SOY = "Soy"
    ALMOND = "Almond"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
