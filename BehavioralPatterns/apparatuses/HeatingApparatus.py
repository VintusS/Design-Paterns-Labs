from enum import Enum


class HeatingApparatus(Enum):
    MICROWAVE = "Microwave"
    CONSTANT_TEMPERATURE_HEATER = "Heater"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value
