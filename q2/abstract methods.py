from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_data(self):
       pass

class TempSensor(Sensor):
    def get_data(self):
        return "24 deg C"
    def __str__(self):
        return "24 deg C"
    
sensor = TempSensor()
print(sensor.get_data())
print(sensor)

"""
from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_data(self):
       pass

class PhSensor(Sensor):
    def get_data(self):
        return "25 deg C"
    def __str__(self):
        return "25 deg C"

class TempSensor(Sensor):
    def get_data(self):
        return "24 deg C"
    def __str__(self):
        return "24 deg C"
    
sensor = TempSensor()
print(sensor.get_data())
print(sensor)
sensoor = PhSensor()
print(sensoor.get_data())
print(sensoor)
"""
