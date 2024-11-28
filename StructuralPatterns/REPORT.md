# Structural Design Patterns


## Author: Mindrescu Dragomir, FAF-221

----

## Objectives:

* Study and understand Structural Design Patterns.
* As a continuation of the previous laboratory work, think about the functionalities that your system will need to provide to the user.
* Implement some additional functionalities usign Structural Design Patterns.
## Theoretical Background 
In software engineering, the Structural Design Patterns are concerned with how classes and objects are composed to form larger structures. Structural class patterns use inheritance to create a hierarchy of classes/abstractions, but the structural object patterns use composition which is generally a more flexible alternative to inheritance.

## Used Design Patterns: 

* Decorator 
* Bridge 
* Composite 
* Flyweight 

## Implementation

The previous version of the project focused more on Creational Design Patterns, that in some way allowed flexibility for creating coffee, but was not really the most scalable approach from a number of considerations. 
The `Coffee` class did not allow for a great flexibility and representation of the objects it is made of, using fields like `milk_type` or `milk_volume` instead of encapsulating those in a `milk` attribute that can later be used.
### Bridge - `Coffee`
One may assume that a more suitable pattern for a `Coffee` class would be a composite, since it allows addign multiple components that implement the same interface. But actually coffee is mostly made out of 3 ingredients - `Beans`, `Milk` and `Topping` which has been changed to `Syrup` with seemingly no reason. 
So it makes more sense to implement a bridge for these `CoffeeIngredients` rather than a composite, so that we can develop in the future the `Milk`, `Beans` and `Syrup` classes separately as abstractions and both implementations.
```python
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

    <getters, base methods overrides>
```
And from here we can work on the `Milk`, `Bean` and `Syrup` classes independently. We can create a `CoffeeIngredient` abstract class, which then will be derived into other specializations.
```python
class CoffeeIngredient(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
```
And we can add available ingredients using inheritance of the base ingredient class. By this approach, I have made available:
* `Milk`
  * `AlmondMilk`
  * `RegularMilk`
* `Bean`
  * `RobustaBean`
  * `ArabicaBean`
* `Syrup`
  * `CoconutSyrup`
  * `VanillaSyrup`

Using the python **built-in** `enum` module, I have also added enumerations of the types of these ingredients, so that a client can select them without the need to call the base class, instead using a builder/factory by selecting the respective value from the enumerations.
### Decorator - `TakeOutCoffee` and `OnThePlaceCoffee` 
We can add bonus functionality to our coffee based on what serving mode does a client select. 
We can start by declaring a base `CoffeeDecorator` class, and derive it and create the `TakeOutCoffeeDecorator` and `OnThePlaceCoffeeDecorator` classes and add modified behaviour for those. 
The `TakeOutCoffeeDecorator` makes a coffee have a lid, that can be taken off or on
```python
class TakeOutCoffeeDecorator(CoffeeDecorator):
    def __init__(self, coffee: Coffee = None) -> None:
        super().__init__(coffee)
        self.lid_on = True

    def get_price(self) -> float:
        return super().get_price()

    def show(self):
        return super().show() + " for take out."

    def get_serving_instructions(self):
        return "Take out"

    def take_lid_off(self):
        self.lid_on = False
        print("Lid taken off")

    def put_lid_on(self):
        self.lid_on = True
        print("Lid put on")
```
and the `OnThePlaceCoffeeDecorator` adds a nice foam art on the coffee.
```python
class OnThePlaceCoffeeDecorator(CoffeeDecorator):
    def __init__(self, coffee: Coffee = None) -> None:
        super().__init__(coffee)
        self.foam_art = "Heart"

    def get_price(self) -> float:
        return super().get_price()

    def get_serving_instructions(self):
        return "On the place"

    def __str__(self) -> str:
        return super().__str__()

    def show(self):
        return super().show() + " with a foam art of a " + self.foam_art.lower()

    def mix(self):
        self.foam_art = "Mixed"
        print("Foam art mixed")
```
The `CoffeeBuilder` class has also been modified with adding 2 new methods, that set a flag for the serving type and will return a decorated objects of the coffee.
### Composite - `Order` 
Since the coffee shop started serving pastry, and some users wanted to order multiple coffees at a time, there appeared the question of easing this process. We can implement an `Order` class that is a composite for the `MenuItem` class and stores the items made in the order:
```python
class Order(MenuItem):
    def __init__(self, items: list[MenuItem] = []) -> None:
        self.items = items
        if len(items) == 0:
            super().__init__("Order", 0)
        else:
            super().__init__(self.get_name(), self.get_price())

    def get_name(self):
        return ', '.join(item.get_name() for item in self.items)

    def add(self, item: MenuItem):
        self.items.append(item)

    def get_price(self) -> float:
        print(self.items)
        return sum(item.get_price() for item in self.items)

    def get_items(self):
        return self.items

    def show(self) -> str:
        return "\n".join(item.show() for item in self.items)

    def __str__(self) -> str:
        return f"Order: {self.get_name()} - {self.get_price()}"
```
The `Order` class implements all methods of the base `MenuItem` class, and encapsulates and eases out the creation of orders that contain multiple items, and also counting the final bill for a client. 
It is enough to call `get_price()` on an order now, rather than iterating multiple items and summing their `get_price()` methods. 
And a user can also access individual items by using an index, calling `get_items()[i]`.
### Flyweight - `CoffeeIngredientFlyweightFactory`
Since we will need to create multiple coffees, it would be logical to store their ingredients in a cached way that will be more memory-efficient and will preserve the base attributes of the instantiated objects, while allowing to modify them in the future as separate instances.
```python
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
``` 
It stores the ingredients in a dictionary and implements lazy object creation, by creating objects only if those are absent and only when needed.
Otherwise, it will return just the object that is already stored in its' memory.

# Result, Usage Example
We can create some coffee for take out using this:
```python
coffee = CoffeeBuilder().with_milk(MilkType.ALMOND).with_bean(
    BeanType.ARABICA).with_syrup(SyrupType.VANILLA).for_take_out().build()

print(coffee.show())
```
which will show:
```
Coffee with Almond Milk with Arabica Beans from Ethiopia with Vanilla flavoured syrup  - 3.25 with lid on
```
or another coffee to be served on the place
```python
another_coffee = CoffeeBuilder().with_milk(MilkType.REGULAR).with_bean(
    BeanType.ROBUSTA).with_syrup(SyrupType.COCONUT).on_the_place().build()
print(another_coffee.show())
```
which will show
```
Coffee with Regular Milk with Robusta Beans from Vietnam with Coconut flavoured syrup  - 2.75 with a foam art of a heart
```
And also create a composite order with some coffee and a croissant (this part was indented for readability, python does not allow such indentation)
```python
order = OrderBuilder().add_coffee(
    CoffeeBuilder()
        .with_milk(MilkType.ALMOND)
        .with_bean(BeanType.ARABICA)
        .with_syrup(SyrupType.VANILLA)
        .build())
    .add_pastry(
    PastryFactory()
        .create_pastry(pastry_type=PastryType.CROISSANT)
    ).build()

print(order.show())
```
which will show the expected:
```
Coffee with Almond Milk with Arabica Beans from Ethiopia with Vanilla flavoured syrup  - 3.25
Croissant - 4.5, 230 calories
```
# Conclusions
This lab was highly beneficial in exploring the practical applications of structural design patterns, which are essential in organizing and managing complex object compositions. 
By implementing patterns like Decorator, Bridge, Composite, and Flyweight, we were able to create a more flexible and scalable system for building coffee products and orders. 
These patterns allow for increased modularity, reducing code duplication and promoting reusability while enhancing flexibility in ingredient representation, customization, and order management. 
Structural design patterns prove valuable in developing systems that require combining multiple elements seamlessly, ensuring efficiency and adaptability in larger-scale applications.