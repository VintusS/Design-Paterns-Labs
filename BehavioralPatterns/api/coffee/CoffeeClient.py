from coffee.enums.BeanType import BeanType
from coffee.enums.MilkType import MilkType
from coffee.enums.SyrupType import SyrupType
from employee.barista.Barista import Barista


class CoffeeClient:
    def __init__(self, barista: Barista) -> None:
        self._barista = barista

    def make(
        self,
        milk: MilkType = None,
        bean: BeanType = None,
        syrup: SyrupType = None,
        take_out: bool = False,
    ):
        return self._barista.handle_request(
            {
                "request": "order",
                "coffee": {
                    "milk": milk,
                    "bean": bean,
                    "syrup": syrup,
                    "take_out": take_out,
                },
            }
        )
