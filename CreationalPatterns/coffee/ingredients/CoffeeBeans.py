from enum import Enum


class CoffeeBeans(Enum):
    ARABICA = "Arabica"
    ROBUSTA = "Robusta"
    LIBERICA = "Liberica"
    EXCELSA = "Excelsa"
    STENOPHILLA = "Stenophylla"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
