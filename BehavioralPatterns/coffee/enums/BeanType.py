from enum import Enum


class BeanType(Enum):
    ARABICA = "Arabica"
    ROBUSTA = "Robusta"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
