from abc import *
class CollegeAutomation(ABC):
    @abstractmethod
    def m1(self):pass
    @abstractmethod
    def m2(self):pass
    @abstractmethod
    def m3(self):pass         
class AbsClass(CollegeAutomation):
    def m1(self):
        print('m1 method implementation')
    def m2(self):
        print('m2 method implementation')

class ConcreteClass(AbsClass):
    def m3(self):
        print('m3 method implementation')

c=ConcreteClass()
c.m1()
c.m2()
c.m3()        