from enum import Enum


class SyrupType(Enum):
    COCONUT = "Coconut"
    VANILLA = "Vanilla"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
