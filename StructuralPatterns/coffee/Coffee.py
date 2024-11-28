from coffee.ingredients.bean.Bean import Bean
from coffee.ingredients.milk.Milk import Milk
from coffee.ingredients.syrup.Syrup import Syrup
from menu.MenuItem import MenuItem


class Coffee(MenuItem):
    def __init__(self, name: str = "Coffee", price: float = 1.0, milk: Milk = None, bean: Bean = None, syrup: Syrup = None) -> None:
        self.base_price = price
        self.milk = milk
        self.bean = bean
        self.syrup = syrup
        super().__init__(name, self.get_price())

    def get_price(self) -> float:
        milk_cost = self.milk.get_cost() if self.milk else 0
        bean_cost = self.bean.get_cost() if self.bean else 0
        syrup_cost = self.syrup.get_cost() if self.syrup else 0
        return milk_cost + bean_cost + syrup_cost + self.base_price

    def get_milk(self) -> Milk:
        return self.milk

    def get_bean(self) -> Bean:
        return self.bean

    def get_syrup(self) -> Syrup:
        return self.syrup

    def __str__(self) -> str:
        milk_str = f" with {self.milk}" if self.milk else ""
        bean_str = f""" with {self.bean.get_name()}s from {
            self.bean.get_origin_country()}""" if self.bean else ""
        syrup_str = f""" with {self.syrup.get_flavour(
        )} flavoured syrup """ if self.syrup else ""
        return f"{self._name}{milk_str}{bean_str}{syrup_str} - {self.get_price()}"

    def show(self):
        return self.__str__()
