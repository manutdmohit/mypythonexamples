from abc import abstractmethod,ABC
class Vehicle(ABC):
    @abstractmethod
    def getNoofWheels(self):pass
class Bus(Vehicle):
    def getNoofWheels(self):
        return 6
class Auto(Vehicle):
    def getNoofWheels(self):
        return 3
b=Bus()
print(b.getNoofWheels())
a=Auto()
print(a.getNoofWheels())                    