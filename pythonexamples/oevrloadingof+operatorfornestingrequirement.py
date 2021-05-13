class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        print('add method execcuted')
        return Book(self.pages+other.pages)
    def __str__(self):
        return 'The total number of pages:{}'.format(self.pages)    
    def __mul__(self,other):
        print('mul method executed')
        return Book(self.pages*other.pages)    

b1=Book(100)
b2=Book(200)
b3=Book(500)
b4=Book(600)
print(b1+b2*b3+b4)


