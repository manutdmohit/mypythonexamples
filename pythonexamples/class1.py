class Student:
	'''Class developed by Durga for Demo'''
	def __init__(self):
		self.name='Durga'
		self.rollno=101
		self.marks=90

	def talk(self):
		print('Hello I am:',self.name)
		print('My roll no:',self.rollno)
		print('My marks are:',self.marks)
s=Student()
print(s.name)
print(s.rollno)
print(s.marks)
s.talk()