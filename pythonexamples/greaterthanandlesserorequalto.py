class Student:
    def __init__(self,name,marks):
        self.name=name 
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks 
    def __le__(self,other):
        return self.marks<=other.marks      
s1=Student('Durga',100)
s2=Student('Ravi',200)
s3=Student('Shiva',50)  
print(s1<=s2)
print(s1>=s2)