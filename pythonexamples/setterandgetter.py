class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

n=int(input('Enter no of students:')) 
students=[]
for i in range(n):
    s=Student()
    name=input('Enter Student Name:') 
    marks=int(input('Enter Marks:'))
    s.setName(name)
    s.setMarks(marks)
    students.append(s)

for s in students:
    print('Hello',s.getName())
    print('Your Marks are:',s.getMarks())
    print()
