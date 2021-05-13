class Engine:
    def __init__(self):
        self.power='125KW'
    def useEngine(self):
        print('Engine Specific Functionality')
class Car:
    def __init__(self):
        self.engine=Engine()
    def usecar(self):
        print('Car required Engine functionality')
        self.engine.useEngine()
        print(self.engine.power)

c=Car()
c.usecar()                    