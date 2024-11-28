from api.CoffeeShopClient import CoffeeShopClient
from coffee.enums.BeanType import BeanType
from coffee.enums.MilkType import MilkType
from coffee.enums.SyrupType import SyrupType
from pastry.enums.PastryType import PastryType


api = CoffeeShopClient()

coffee = api.coffee.make(
    milk=MilkType.REGULAR, bean=BeanType.ARABICA, syrup=SyrupType.VANILLA, take_out=True
)


order = api.orders.new()

order = api.orders.add_coffee(
    order=order,
    milk=MilkType.REGULAR,
    bean=BeanType.ARABICA,
    syrup=SyrupType.VANILLA,
    to_go=True,
)

order = api.orders.add_pastry(order=order, pastry_type=PastryType.CROISSANT)
order = api.orders.add_pastry(order=order, pastry_type=PastryType.PAIN_AU_CHOCOLAT)
order = api.orders.add_coffee(
    order=order,
    milk=MilkType.REGULAR,
    bean=BeanType.ARABICA,
    syrup=SyrupType.VANILLA,
    to_go=True,
)
order = api.orders.add_coffee(order=order, bean=BeanType.ROBUSTA)
print(order.show())
