from coffee.enums.MilkType import MilkType
from coffee.enums.BeanType import BeanType
from coffee.enums.SyrupType import SyrupType
from coffee.ingredients.bean.RobustaBean import RobustaBean
from coffee.ingredients.bean.ArabicaBean import ArabicaBean
from coffee.ingredients.milk.AlmondMilk import AlmondMilk
from coffee.ingredients.milk.RegularMilk import RegularMilk
from coffee.ingredients.syrup.CoconutSyrup import CoconutSyrup
from coffee.ingredients.syrup.VanillaSyrup import VanillaSyrup


class CoffeeIngredientFlyweightFactory:
    def __init__(self):
        self._ingredients = {}

    def get_ingredient(self, ingredient_type):
        if ingredient_type not in self._ingredients:
            if ingredient_type == MilkType.ALMOND:
                self._ingredients[ingredient_type] = AlmondMilk()
            elif ingredient_type == MilkType.REGULAR:
                self._ingredients[ingredient_type] = RegularMilk()
            elif ingredient_type == BeanType.ARABICA:
                self._ingredients[ingredient_type] = ArabicaBean()
            elif ingredient_type == BeanType.ROBUSTA:
                self._ingredients[ingredient_type] = RobustaBean()
            elif ingredient_type == SyrupType.VANILLA:
                self._ingredients[ingredient_type] = VanillaSyrup()
            elif ingredient_type == SyrupType.COCONUT:
                self._ingredients[ingredient_type] = CoconutSyrup()
            else:
                raise ValueError(f"Unknown ingredient type: {ingredient_type}")

        return self._ingredients[ingredient_type]
