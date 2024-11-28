from employee.StatefulEmployee import StatefulEmployee
from employee.barista.BaristaBreakState import BaristaBreakState
from employee.barista.BaristaReadyState import BaristaReadyState
from employee.barista.BaristaContext import BaristaContext


class Barista(StatefulEmployee):
    def __init__(self, name: str = None) -> None:
        super().__init__(name)
        self._context = BaristaContext()
        self.add_state(
            key="ready", state=BaristaReadyState(barista_context=self._context)
        )
        self.add_state(key="break", state=BaristaBreakState())
        self.set_ready_state()

    def set_ready_state(self):
        self._context.reset_fatigue()
        self.set_state(key="ready")

    def set_break_state(self):
        self.set_state(key="break")

    def handle_request(self, request: dict):
        if self._context.get_fatigue() < 3:
            return self.current_state.handle_request(request)
        else:
            self.set_break_state()
            self.current_state.handle_request(request)
            self.set_ready_state()
            return self.handle_request(request)

    def __str__(self) -> str:
        return f"Barista: {self.name} - current state: {self.current_state}"

    def __repr__(self) -> str:
        return super().__str__()
