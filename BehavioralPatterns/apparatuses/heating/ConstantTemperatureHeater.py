class ConstantTemperatureHeater:
    def __init__(self):
        self.is_on = False
        self.working_temperature = 40

    def heat(self, object: any):
        if hasattr(object, "temperature"):
            object.temperature = self.working_temperature
        return object

    def turn_on(self):
        self.is_on = True
        return self

    def turn_off(self):
        self.is_on = False
        return self
