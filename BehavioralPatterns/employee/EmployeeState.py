from abc import ABC, abstractmethod


class EmployeeState(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass
