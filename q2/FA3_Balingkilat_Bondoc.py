from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
       pass

class PhSensor(Sensor):
    def get_reading(self):
        return "7.2 pH (Neutral)"
    def __str__(self):
        return "7.2 pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self):
        return "24.5°C"
    def __str__(self):
        return "24.5°C"
    
sensor = TempSensor()
sensoor = PhSensor()
print("---Lab Inventory System---")
print(f"[pH Sensor] Reading:", sensor)
print(f"[Temperature Sensor] Reading:", sensoor)
print()
print("----------------------------")
#my_sensor = Sensor()
