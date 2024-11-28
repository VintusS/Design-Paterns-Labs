class Microwave:
    def __init__(self, temperature):
        self.temperature = temperature
        self.is_on = False

    def set_temperature(self, temperature):
        self.temperature = temperature
        return self

    def turn_on(self):
        self.is_on = True
        return self

    def turn_off(self):
        self.is_on = False
        return self

    def start_warming(self, object: any):
        if hasattr(object, "temperature"):
            object.temperature = self.temperature
        return object
