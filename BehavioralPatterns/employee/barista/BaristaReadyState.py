from employee.EmployeeState import EmployeeState
from coffee.creators.builder.CoffeeBuilder import CoffeeBuilder
from employee.barista.BaristaContext import BaristaContext


class BaristaReadyState(EmployeeState):
    def __init__(self, barista_context: BaristaContext = None) -> None:
        super().__init__()
        self.name = "Ready"
        self._builder = CoffeeBuilder()
        self._barista_context = barista_context

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

    def __str__(self) -> str:
        return f"Barista state: {self.name}"

    def __repr__(self) -> str:
        return self.__str__()

    def _decode_request(self, request: dict):
        pass
