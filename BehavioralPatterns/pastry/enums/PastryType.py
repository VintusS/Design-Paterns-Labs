from enum import Enum


class PastryType(Enum):
    CROISSANT = "CROISSANT"
    PAIN_AU_CHOCOLAT = "PAIN_AU_CHOCOLAT"

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(pastry_type_str):
        for pastry_type in PastryType:
            if pastry_type_str.upper() == str(pastry_type):
                return pastry_type
            elif pastry_type_str.upper() == pastry_type.value:
                return pastry_type
            elif pastry_type_str.upper() == pastry_type.name:
                return pastry_type
        raise ValueError(f"Invalid pastry type: {pastry_type_str}")

    def __repr__(self) -> str:
        return super().__repr__()
