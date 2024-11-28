from pastry.Pastry import Pastry
from pastry.enums.PastryType import PastryType
from pastry.Croissant import Croissant
from pastry.PainAuChocolat import PainAuChocolat


class PastryFactory:
    def __init__(self) -> None:
        self.pastry_types_hashmap = {
            PastryType.CROISSANT: Croissant,
            PastryType.PAIN_AU_CHOCOLAT: PainAuChocolat,
        }

    def create_pastry(self, pastry_type: PastryType) -> Pastry:
        if pastry_type in self.pastry_types_hashmap:
            return self.pastry_types_hashmap[pastry_type]()
        else:
            print(f"Invalid pastry type: {pastry_type}")
