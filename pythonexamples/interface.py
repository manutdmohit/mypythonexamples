from abc import *
class CollegeAutomation(ABC):
    @abstractmethod
    def m1(self):pass
    @abstractmethod
    def m2(self):pass
    @abstractmethod
    def m3(self):pass
    @abstractmethod
    def m4(self):pass
class DurgaSoftImpl(CollegeAutomation):
    def m1(self):
        print('m1 method implemenation')
    def m2(self):
        print('m2 method implemenation')        
    def m3(self):
        print('m3 method implemenation')    
    def m4(self):
        print('m4 method implemenation')    
d=DurgaSoftImpl()
d.m1()
d.m2()
d.m3()
d.m4()

