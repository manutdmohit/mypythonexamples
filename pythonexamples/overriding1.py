class Person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('Height:',self.height)
        print('Weight:',self.weight) 
class Employee(Person):
    def __init__(self,name,age,height,weight,eno,esal):
        super().__init__(name,age,height,weight)
        self.eno=eno
        self.esal=esal      
    def display(self):
        super().display()
        print('Employee Number:',self.eno)
        print('Employee Salary:',self.esal)      
e=Employee('Durga',48,5.5,68,8888,50000)  
e.display()     
