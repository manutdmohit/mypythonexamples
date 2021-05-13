class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def __str__(self):
        return 'Name:{},RollNo:{},Marks:{}'.format(self.name,self.rollno,self.marks)    

s1=Student('Durga',101,98)
s2=Student('Ravi',102,88)        
print(s1)
print(s2)
