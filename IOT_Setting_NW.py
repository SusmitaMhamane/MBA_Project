class Sensor:
    def __init__(self, name):
        self.name = name

    def get_reading(self):
        pass

class TemperatureSensor(Sensor):
    def get_reading(self):
        # Simulate temperature reading
        return 25.0  # Placeholder value

class HumiditySensor(Sensor):
    def get_reading(self):
        # Simulate humidity reading
        return 60.0  # Placeholder value
