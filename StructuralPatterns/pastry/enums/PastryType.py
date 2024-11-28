from enum import Enum


class PastryType(Enum):
    CROISSANT = "Croissant"
    PAIN_AU_CHOCOLAT = "Pain au Chocolat"

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(pastry_type_str):
        for pastry_type in PastryType:
            if pastry_type_str.lower() == str(pastry_type).lower():
                return pastry_type
        raise ValueError(f"Invalid pastry type: {pastry_type_str}")

    def __repr__(self) -> str:
        return super().__repr__()
