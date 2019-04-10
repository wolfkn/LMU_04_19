from controller.simple_daq import SimpleDaq

from model import ur

class AnalogDaq:
    def __init__(self, port, resistance):
        self.driver = SimpleDaq(port)
        self.resistance = resistance

    def read_current(self, channel):
        voltage = self.driver.get_analog_value(channel)
        voltage = voltage/1023*ur('3.3V')
        current = voltage/self.resistance
        return current

    def set_voltage(self, channel, voltage):
        self.driver.set_analog_value(channel, voltage)

    def finish(self):
        self.driver.set_analog_value(0, 0)
        self.driver.set_analog_value(1, 0)
        self.driver.finalize()

