from coffee.Coffee import Coffee
from coffee.ingredients.bean.ArabicaBean import ArabicaBean
from coffee.ingredients.milk.AlmondMilk import AlmondMilk
from coffee.ingredients.syrup.VanillaSyrup import VanillaSyrup
from menu.Menu import Menu
from pastry.Pastry import Pastry
from pastry.enums.PastryType import PastryType
from coffee.enums.BeanType import BeanType
from coffee.enums.MilkType import MilkType
from coffee.enums.SyrupType import SyrupType
from coffee.creators.builder.CoffeeBuilder import CoffeeBuilder
from order.builder.OrderBuilder import OrderBuilder
from pastry.PastryFactory import PastryFactory

coffee = CoffeeBuilder().with_milk(MilkType.ALMOND).with_bean(
    BeanType.ARABICA).with_syrup(SyrupType.VANILLA).for_take_out().build()

print(coffee.show())

another_coffee = CoffeeBuilder().with_milk(MilkType.REGULAR).with_bean(
    BeanType.ROBUSTA).with_syrup(SyrupType.COCONUT).on_the_place().build()
print(another_coffee.show())


order = OrderBuilder().add_coffee(CoffeeBuilder().with_milk(MilkType.ALMOND).with_bean(
    BeanType.ARABICA).with_syrup(SyrupType.VANILLA).build()).add_pastry(PastryFactory().create_pastry(pastry_type=PastryType.CROISSANT)).build()


print(order.show())
