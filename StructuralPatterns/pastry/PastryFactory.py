from pastry.Pastry import Pastry
from pastry.enums.PastryType import PastryType
from pastry.Croissant import Croissant
from pastry.PainAuChocolat import PainAuChocolat


class PastryFactory():
    def __init__(self) -> None:
        pass

    def create_pastry(self, pastry_type: PastryType) -> Pastry:
        if pastry_type == PastryType.CROISSANT:
            return Croissant()
        elif pastry_type == PastryType.PAIN_AU_CHOCOLAT:
            return PainAuChocolat()
        else:
            raise ValueError(f"Invalid pastry type: {pastry_type}")
