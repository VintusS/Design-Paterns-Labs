# Structural Design Patterns


## Author: Mindrescu Dragomir, FAF-221

----

## Objectives:

* Study and understand Behavioral Design Patterns.
* As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system.
* Implement at least 1 Behavioral Design Pattern that extends the functionality of the system.
* There should only be one client for the whole system.
* The behavioral DPs can be integrated into you functionalities alongside the structural ones.

## Theoretical Background 
In software engineering, behavioral design patterns have the purpose of identifying common communication patterns between different software entities. By doing so, these patterns increase flexibility in carrying out this communication.

## Used Design Patterns: 

* State 

## Implementation
Since this system focuses mostly on creating instances of items and managing resources and data, it may be hard to fit Behavioral patterns in an organic way. However, we may be creative about that and find some places we can improve the system.
### State - `Barista`
The barista class implements the `StatefulEmployee` class, which indicates that this abstract class makes use of different states to represent the behavior of an Employee.
```python
class Barista(StatefulEmployee):
    def __init__(self, name: str = None) -> None:
        super().__init__(name)
        self._context = BaristaContext()
        self.add_state(
            key="ready", state=BaristaReadyState(barista_context=self._context)
        )
        self.add_state(key="break", state=BaristaBreakState())
        self.set_ready_state()
```
We will also need a simple abstract class, named `EmployeeState`, that will serve as a contract of the methods for the states to implement.
```python
class EmployeeState(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass
```
Which we can then derive into the classes

#### [`BaristaReadyState`](https://github.com/Flexksx/Design-Patterns-Labs/blob/64362b0044129f5d990d709e425f6e4742e1a7d7/BehavioralPatterns/employee/barista/BaristaReadyState.py)
Which will decode a dictionary and act as an adapter between a dictionary and the methods of the previously created `CoffeBuilder` class. It will also use the shared `BaristaContext` object to increment the fatigue of the `Barista`, which will trigger a state change in it.
```python
def handle_request(self, request: dict):
        if request["request"] != "order":
            print("Barista can only handle orders.")
        if "coffee" not in request:
            print("Barista needs a coffee order to proceed.")
        else:
            if "milk" in request["coffee"]:
                self._builder.with_milk(request["coffee"]["milk"])
            if "bean" in request["coffee"]:
                self._builder.with_bean(request["coffee"]["bean"])
            if "syrup" in request["coffee"]:
                self._builder.with_syrup(request["coffee"]["syrup"])
            if "take_out" in request["coffee"]:
                if request["coffee"]["take_out"]:
                    self._builder.for_take_out()
                else:
                    self._builder.on_the_place()
            coffee = self._builder.build()
            print("Barista has made the coffee: " + coffee.show())
            self._barista_context.increment_fatigue()
            return coffee
```
#### [`BaristaBreakState`](https://github.com/Flexksx/Design-Patterns-Labs/blob/64362b0044129f5d990d709e425f6e4742e1a7d7/BehavioralPatterns/employee/barista/BaristaBreakState.py)
This class will make the user wait 2 seconds for the barista to have a break and print an ascii art and a progress bar for the time waiting. The barista will also not handle the request, since they're on a break.
```python
def handle_request(self, request: dict):
        print(self.ascii_art)
        iterations = 100
        duration = 2
        interval = duration / iterations

        for _ in tqdm(
            range(iterations),
            desc="Taking a Break",
            ncols=50,
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
        ):
            time.sleep(interval)
``` 
In the `Barista` class, the `handle_request` method will brew a coffee if the fatigue is less than 3, and then it will let the barista have a break, after which it will handle the request again.
```python
def handle_request(self, request: dict):
        if self._context.get_fatigue() < 3:
            return self.current_state.handle_request(request)
        else:
            self.set_break_state()
            self.current_state.handle_request(request)
            self.set_ready_state()
            return self.handle_request(request)
```
### Single client implementation
The structure of the client was inspired by the OpenAI python library, which encapsulates different parts of their API into clearly separated parts, and the developer accesses those as attributes and methods.
In the same way, I have created the `CoffeeShopClient` class
```python
class CoffeeShopClient:
    def __init__(self) -> None:
        self._barista = Barista(name="John")
        self.coffee = CoffeeClient(barista=self._barista)
        self.pastry = PastryClient()
        self.orders = OrderClient(coffee_client=self.coffee, pastry_client=self.pastry)
```
where the `PastryClient` and `CoffeeClient` have the responsibility of creating items at method call, and the `OrderClient` is responsible for initializing and modifying (adding items) to existing `Order` objects.

## Result
We have to initialize the client with
```python
api = CoffeeShopClient()
```
after which we can call it's submodules, like for making a coffee
```python
coffee = api.coffee.make(
    milk=MilkType.REGULAR, bean=BeanType.ARABICA, syrup=SyrupType.VANILLA, take_out=True
)
```
Or we can create an order and add some coffees and deserts to it
```python
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
```
Which show the following output
```
Barista has made the coffee: Coffee with Regular Milk with Arabica Beans from Ethiopia with Vanilla flavoured syrup  - 3.0 with lid on
Barista has made the coffee: Coffee with Regular Milk with Arabica Beans from Ethiopia with Vanilla flavoured syrup  - 3.0 with lid on
Added coffee to order
Added pastry to order
Added pastry to order
Barista has made the coffee: Coffee with Regular Milk with Arabica Beans from Ethiopia with Vanilla flavoured syrup  - 3.0 with lid on
Added coffee to order         
Taking a Break: 100%|████████████████████| 100/100
Barista has made the coffee: Coffee with Robusta Beans from Vietnam - 1.75 with lid on
Added coffee to order
Coffee with Regular Milk with Arabica Beans from Ethiopia with Vanilla flavoured syrup  - 3.0 with lid on
Croissant - 4.5, 230 calories
Pain au chocolat - 3.5, 300 calories
Coffee with Regular Milk with Arabica Beans from Ethiopia with Vanilla flavoured syrup  - 3.0 with lid on
Coffee with Robusta Beans from Vietnam - 1.75 with lid on
```
# Conclusions
This laboratory work focused on implementing the State design pattern for the `Barista` class, which also allows us in the future to add other `StatefulEmployees` by deriving the respective abstract class. The State pattern also allows the developers to add other states for the employee or modifying the behaviour of concrete states in the future.
This assignment also emphasizes on the importance of using behavioral patterns of different types to achieve good results in terms of extendability of the project and the robustness of a system. 
By creating a well-structured project from the start, it is very easy to implement new features without the need to add breaking changes and avoiding smelly code.