class Person:
    def __init__(self,name,dd,mm,yyyy):
        print('Person Object created')
        self.name=name
        self.dob=self.Dob(dd,mm,yyyy)
    def info(self):
        print('Name:',self.name)
        self.dob.display()    
    class Dob:
        def __init__(self,dd,mm,yyyy):
            print('DOB object created')
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
        def display(self):
            print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyyy))
p=Person('Durga',8,9,1996)
p.info()            