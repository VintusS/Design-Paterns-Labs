from typing import Union
from coffee.creators.flyweight.CoffeeIngredientFlyweightFactory import CoffeeIngredientFlyweightFactory
from coffee.Coffee import Coffee
from coffee.ingredients.bean.Bean import Bean
from coffee.ingredients.milk.Milk import Milk
from coffee.ingredients.syrup.Syrup import Syrup
from coffee.enums.SyrupType import SyrupType
from coffee.enums.BeanType import BeanType
from coffee.enums.MilkType import MilkType
from coffee.decorator.OnThePlaceCoffeeDecorator import OnThePlaceCoffeeDecorator
from coffee.decorator.TakeOutCoffeeDecorator import TakeOutCoffeeDecorator


class CoffeeBuilder:
    def __init__(self) -> None:
        self._milk: Milk = None
        self._bean: Bean = None
        self._syrup: Syrup = None
        self._serving_type: str = None

    def with_milk(self, milk_type: MilkType):
        self._milk = CoffeeIngredientFlyweightFactory().get_ingredient(milk_type)
        return self

    def with_bean(self, bean_type: BeanType):
        self._bean = CoffeeIngredientFlyweightFactory().get_ingredient(bean_type)
        return self

    def with_syrup(self, syrup: SyrupType):
        self._syrup = CoffeeIngredientFlyweightFactory().get_ingredient(syrup)
        return self

    def for_take_out(self):
        self._serving_type = 'take_out'
        return self

    def on_the_place(self):
        self._serving_type = 'on_the_place'
        return self

    def build(self):
        coffee = Coffee(milk=self._milk, bean=self._bean, syrup=self._syrup)

        if self._serving_type == 'take_out':
            return TakeOutCoffeeDecorator(coffee)
        elif self._serving_type == 'on_the_place':
            return OnThePlaceCoffeeDecorator(coffee)

        return coffee
