class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getInfo(self):
        print('Car Name:{},Model:{},Color:{}'.format(self.name,self.model,self.color))

class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    def empInfo(self):
        print('Employee Name:',self.ename)
        print('Employee Number:',self.eno)
        print('Employee Car Info')    
        self.car.getInfo()

car=Car('Innova','2.5v','Grey')
emp=Employee('Durga',872425,car)
emp.empInfo()

