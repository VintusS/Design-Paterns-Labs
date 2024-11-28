from apparatuses.HeatingApparatus import HeatingApparatus
from apparatuses.heating.ConstantTemperatureHeater import ConstantTemperatureHeater
from apparatuses.heating.Microwave import Microwave
from menu.MenuItem import MenuItem


class HeatingAdapter:
    def __init__(self) -> None:
        self.microwave = Microwave(40)
        self.heater = ConstantTemperatureHeater()

    def warm(self, apparatus: HeatingApparatus = HeatingApparatus.MICROWAVE, product: MenuItem = None):
        if apparatus == HeatingApparatus.MICROWAVE:
            self.microwave.turn_on()
            self.microwave.set_temperature(40)
            heated_product = self.microwave.start_warming(product)
            self.microwave.turn_off()
            return heated_product
        elif apparatus == HeatingApparatus.CONSTANT_TEMPERATURE_HEATER:
            self.heater.turn_on()
            heated_product = self.heater.heat(product)
            self.heater.turn_off()
            return heated_product

    def hot(self, product: MenuItem = None):
        self.microwave.turn_on()
        self.microwave.set_temperature(100)
        heated_product = self.microwave.start_warming(product)
        self.microwave.turn_off()
        return heated_product
