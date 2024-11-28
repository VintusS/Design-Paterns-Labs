from abc import ABC, abstractmethod

from employee.EmployeeState import EmployeeState


class StatefulEmployee(ABC):
    def __init__(self, name: str = None) -> None:
        self.name = name
        self.possible_states: dict[str, EmployeeState] = {}
        self.current_state = None

    def get_name(self) -> str:
        return self.name

    def add_state(self, key: str = None, state: EmployeeState = None):
        self.possible_states[key] = state

    def set_state(self, key: str = None):
        self.current_state = self.possible_states[key]

    def get_current_state(self) -> EmployeeState:
        return self.current_state

    @abstractmethod
    def handle_request(self, request: dict):
        pass

    def __str__(self) -> str:
        return f"Employee: {self.name} - current state: {self.current_state}"

    def __repr__(self) -> str:
        return super().__str__()
