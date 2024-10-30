# Creational Design Patterns


## Author: Mindrescu Dragomir, FAF-221

----

## Objectives:

* Get familiar with the Creational DPs;
* Choose a specific domain;
* Implement at least 3 CDPs for the specific domain;


## Used Design Patterns: 

* Singleton
* Factory
* Builder
* Prototype

## Implementation

To accomplish this lab assignment and to showcase the use of different creational design patterns, I have decided to create a coffee shop simulation.
Coffee is a drink that has multiple varieties and styles of making, mostly differentiating in use of milk, added water, the amount of pure espresso shots and their toppings.

### Singleton - `Menu`
When you want to grab a coffee, you first have to decide what kind of coffee you want. To do that, you look on a menu, that lists the types of drinks available, along with some other details. And there is only one truly truthful menu, that everyone looks at.
This approach allows to addresses the problem of having a centralized, globally accessible list of available coffee items.
By using this pattern, we ensure that there is only one instance of a menu that can be accessed throughout the whole system.
I will show an example of how this helps further.
```python
class Menu:
    _instance = None

    def __init__(self):
        if Menu._instance is not None:
            raise Exception("This is a Singleton class.")
        self._menu_items: list[MenuItem] = []
        Menu._instance = self

    @staticmethod
    def get_instance():
        if Menu._instance is None:
            Menu._instance = Menu()
        return Menu._instance

    def add_menu_item(self, item: MenuItem = None):
        if item is None:
            raise Exception("Passed a NONE item.")
        else:
            self._menu_items.append(item)

    def get_menu_item(self, menu_item_name: str = None):
        for item in self._menu_items:
            if item.name == menu_item_name:
                return item
        print(f"Item {menu_item_name} not found in the menu.")
        return None

    def get_menu_items(self):
        return self._menu_items

    def __repr__(self) -> str:
        menu_string = "[MENU HAS THE FOLLOWING ITEMS]\n"
        for i, item in enumerate(self._menu_items):
            menu_string += f"{i+1}. {item}\n"
        return menu_string
```

### Prototype - `MenuItem` and `CoffeeMenuItem`
When looking on a menu, it shows different types of coffee available at the shop. When you order a coffee, a barista will recreate a physical coffee identically to it's abstract representation listed on a `Menu`.
```python
class MenuItem():
    def __init__(self, name: str = None, price: float = None) -> None:
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def clone(self):
        return copy.deepcopy(self)

    def __repr__(self) -> str:
        return f"{self._name} - {self._price}"
```
This helps with the case that when someone orders a plain espresso or americano, it's actually easier to clone one identical to that on the menu. To define a coffee structure, we can derive the `MenuItem` class into a `CoffeeMenuItem`:
```python
class CoffeeMenuItem(MenuItem):
    def __init__(self,
                 name: str = None,
                 price: float = None,
                 type: DefaultCoffeeType = None,
                 beans: CoffeeBeans = CoffeeBeans.ARABICA,
                 toppings: Topping = None,
                 milk_quantity: float = 0.0,
                 milk_type: MilkType = None,
                 size: CoffeeSize = None) -> None:
        super().__init__(name, price)
        self._type = type
        self._beans = beans
        self._milk_quantity = milk_quantity
        self._milk_type = milk_type
        self._size = size
        self._toppings = toppings

    @property
    def toppings(self):
        return self._toppings

    @property
    def milk_type(self):
        return self._milk_type

    @property
    def coffee_type(self):
        return self._type

    @property
    def size(self):
        return self._size

    @property
    def milk_quantity(self):
        return self._milk_quantity

    @property
    def beans(self):
        return self._beans

    def __repr__(self) -> str:
        return f"A {self._size} {self._type} with {self._beans} beans, {self._milk_quantity}ml of {self._milk_type} milk and {self._toppings} - {self._price}"
```
Which is a template for an actual coffee. Even though there are a lot of types of coffee, we can define some most common ordered ones, like an `Americano`, `Espresso`, `Cappuccino` and a `Latte` that vary in their size and milk quantity.
```python
class Espresso(CoffeeMenuItem):
    def __init__(self):
        super().__init__(name="Espresso",
                         price=1.99,
                         type=DefaultCoffeeType.ESPRESSO,
                         size=CoffeeSize.SMALL)

class Americano(CoffeeMenuItem):
    def __init__(self):
        super().__init__(name="Americano",
                         price=2.49,
                         type=DefaultCoffeeType.AMERICANO,
                         size=CoffeeSize.MEDIUM)

class Cappuccino(CoffeeMenuItem):
    def __init__(self):
        super().__init__(name="Cappuccino",
                         price=3.49,
                         type=DefaultCoffeeType.CAPPUCCINO,
                         milk_quantity=100.0,
                         milk_type=MilkType.WHOLE,
                         size=CoffeeSize.MEDIUM)

class Latte(CoffeeMenuItem):
    def __init__(self):
        super().__init__(name="Latte",
                         price=4.99,
                         type=DefaultCoffeeType.LATTE,
                         milk_quantity=200.0,
                         milk_type=MilkType.WHOLE,
                         size=CoffeeSize.MEDIUM)
```
Notice that there are default types of milk and beans used when preparring coffee. Our shop serves `ARABICA` beans by default, but a customer could specify that they want another kind of beans when ordering.

### Builder - `OrderBuilder` and `CoffeeBuilder`
A customer will come up and make an order. To make the order creation easier, we can use the builder pattern instead of collecting the parameters needed for an `Order` instantiation using other classes, or directly calling an order item. This plainly makes it safer and defines an interface that we can address when customers order coffee.
```python
class OrderBuilder:
    def __init__(self):
        self.coffee_type = None
        self.size = None
        self.toppings = None
        self.beans = None
        self.milk = None

    def of_type(self, coffee_type):
        self.coffee_type = coffee_type
        return self

    def with_size(self, size):
        self.size = size
        return self

    def with_beans(self, beans):
        self.beans = beans
        return self

    def with_milk(self, milk):
        self.milk = milk
        return self

    def with_topping(self, topping):
        self.toppings = topping
        return self

    def build(self):
        if self.coffee_type is None:
            raise ValueError(
                "Cannot brew coffee without specifying a base type of it.")
        return Order(
            coffee_type=self.coffee_type,
            size=self.size,
            toppings=self.toppings,
            beans=self.beans,
            milk=self.milk
        )
```
Using this pattern we can make orders like:
```python
order = OrderBuilder().of_type(DefaultCoffeeType.CAPPUCCINO).with_size(CoffeeSize.LARGE).with_beans(
    CoffeeBeans.ROBUSTA).with_milk(MilkType.SOY).with_topping(Topping.CINNAMON).build()
```
and simpler orders like
```python
order = OrderBuilder().of_type(DefaultCoffeeType.AMERICANO).build()
```
Notice that we do not serve fully custom drinks, but instead we are using a template like a `Cappuccino` and allow configuration of it, like selecting other beans, other milk, a larger size and topping it with some cinnamon. This helps a barista understand what should they start from when fulfilling the order.
So we can have a `CoffeeBuilder` looking like this: 
```python
class CoffeeBuilder:
    def __init__(self) -> None:
        self.modifiying_type: CoffeeMenuItem = None
        self.size = None
        self.beans = None
        self.milk = None
        self.toppings = None
        self.milk_quantity = None
        self.price = None
        self.name = None

    def from_type(self, coffee_type: CoffeeMenuItem):
        self.modifiying_type = coffee_type
        self.size = self.modifiying_type.size
        self.beans = self.modifiying_type.beans
        self.milk = self.modifiying_type.milk_type
        self.toppings = self.modifiying_type.toppings
        self.milk_quantity = self.modifiying_type.milk_quantity
        self.name = self.modifiying_type.name
        self.price = self.modifiying_type.price
        return self

    def with_size(self, size: CoffeeSize = None):
        if size is not None and size != self.modifiying_type.size:
            self.size = size
            if self.size == CoffeeSize.SMALL:
                self.milk_quantity = self.modifiying_type.milk_quantity / 2
            elif self.size == CoffeeSize.LARGE:
                self.milk_quantity = self.modifiying_type.milk_quantity * 1.5
                # Increase the price only on large size, late stage capitalism
                self.price = self.modifiying_type.price * 1.2
        return self

    def with_beans(self, beans: CoffeeBeans = None):
        self.beans = beans
        return self

    def with_milk(self, milk: MilkType = None):
        self.milk = milk
        return self

    def with_topping(self, toppings: Topping = None):
        self.toppings = toppings
        return self

    def build(self):
        return CoffeeMenuItem(
            name=self.name,
            price=self.price,
            type=self.modifiying_type.coffee_type,
            size=self.size,
            beans=self.beans,
            milk_type=self.milk,
            milk_quantity=self.milk_quantity,
            toppings=self.toppings,
        )
```
This builder will take the template of a coffee and start with the base of it, and apply different changes based on the `Order` configuration. For example, it will raise the `price` by 20% and the `milk_quantity` by 50% if you request a `LARGE` coffee.
Since the default `CoffeeMenuItem` is created with 0 milk, if the base we are starting of has no milk, then the result will also have no milk. How can someone order an americano with milk?

### Factory
Since customers can choose among default coffee types, we should allow for an easier creation of those. This is done by employing the `Prototype` pattern we used in the `CoffeeMenuItem` and cloning it based on the `DefaultCoffeeType` requested by the user.
This choice has several benefits - you can pass a value of the enum or the enum value itself, and you'll get a full deep copy of the same `CoffeeMenuItem` you ordered. 
We also employ the `Menu` singleton pattern here, by looking through all available types of coffee in a menu to instantiate a map of `str:CoffeeMenuItem`, to be able to quickly clone it when requested. Another way of using a factory is by using a `switch` statement, or in python - `if elif elif elif` to create objects. But a hashmap follows the same logic, and in our case allows for changing only the menu, instead of changing the `Menu` and the `CoffeeFactory` class when we add some new types.
Also a factory takes in an order item, which has the `.is_basic` property, that indicates that the requested drink represents only a `DefaultCoffeeType` without any customization, which helps us serving the drink in a simpler way. Otherwise, it will pass the order to a builder.
```python
class CoffeeFactory:
    def __init__(self):
        menu = Menu.get_instance()
        menu_items = menu.get_menu_items()
        self._coffee_types = {}
        for item in menu_items:
            item_coffee_type = item.coffee_type.value
            item_prototype = item
            self._coffee_types[item_coffee_type] = item_prototype

    def create_coffee(self, order: Order):
        if order.is_basic:
            return self._coffee_types[order.coffee_type.value].clone()
        else:
            coffee_builder = CoffeeBuilder()
            coffee_builder.from_type(
                self._coffee_types[order.coffee_type.value])
            coffee_builder.with_size(order.size)
            coffee_builder.with_beans(order.coffee_beans)
            coffee_builder.with_milk(order.milk)
            coffee_builder.with_topping(order.toppings)
            return coffee_builder.build()
```

## Result, Usage Example
We will have some default items added to our menu and we will order a custom cappuccino and a plain americano.
```python
menu = Menu.get_instance()
americano = Americano()
cappuccino = Cappuccino()
latte = Latte()
espresso = Espresso()

menu.add_menu_item(americano)
menu.add_menu_item(cappuccino)
menu.add_menu_item(latte)
menu.add_menu_item(espresso)
coffee_factory = CoffeeFactory()

print(menu)

custom_order = OrderBuilder().of_type(DefaultCoffeeType.CAPPUCCINO).with_size(CoffeeSize.LARGE).with_beans(
    CoffeeBeans.ROBUSTA).with_milk(MilkType.SOY).with_topping(Topping.CINNAMON).build()
print(custom_order)
custom_coffee = coffee_factory.create_coffee(custom_order)
print(custom_coffee)

plain_americano_order = OrderBuilder().of_type(
    DefaultCoffeeType.AMERICANO).build()
print(plain_americano_order)
plain_americano_coffee = coffee_factory.create_coffee(plain_americano_order)
print(plain_americano_coffee)
```
Which will produce this output: 
```
[MENU HAS THE FOLLOWING ITEMS]
1. Medium Americano with Arabica beans - 2.99
2. Medium Cappuccino with Arabica beans on Whole milk 100.0 - 3.99
3. Medium Latte with Arabica beans on Whole milk 200.0 - 2.99
4. Small Espresso with Arabica beans - 1.99

Order of a Large Cappuccino with  Robusta beans on Soy milk and Cinnamon on top
Large Cappuccino with Robusta beans on Soy milk 150.0 and Cinnamon - 4.788
Order of a Americano
Medium Americano with Arabica beans - 2.99
```

## Conclusions
In conclusion, this lab assignment not only allowed me to better understand the creational design patterns but also to see their practical value in real-world applications. 
Through the careful implementation of these patterns, I was able to create a flexible, efficient, and scalable system that could accommodate both simple and complex coffee orders, while ensuring consistency and reusability of code. 
This exercise has reinforced the importance of choosing the right pattern for the right problem and demonstrated how design patterns can significantly enhance the maintainability and clarity of a software project.