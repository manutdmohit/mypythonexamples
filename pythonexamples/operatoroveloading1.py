class Employee:
    def __init__(self,name,salaryPerDay):
        self.name=name
        self.salaryPerDay=salaryPerDay
    def __mul__(self,other):
        return (self.salaryPerDay*other.workingDays)    
class TimeSheet:
    def __init__(self,name,workingDays):
        self.name=name
        self.workingDays=workingDays

e=Employee('Durga',500)
t=TimeSheet('Durga',25)
print('This Month Salary:',e*t)

