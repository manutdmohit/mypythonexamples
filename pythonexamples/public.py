class Test:
    def __init__(self):
        self.x=10
    def m1(self):
        print('It is Public Method')
    def m2(self):
        print(self.x)
        self.m1() 

t=Test()
t.m2() 
print(t.x)
t.m1()
              