class P:
    a=10
    def __init__(self):
        print('Parent Constructor')
        self.b=20
    def m1(self):
        print('Parent Instance Method')
    @classmethod
    def m2(cls):
        print('Parent Class Method') 
    @staticmethod
    def m3():
        print('Parent Static Method')   

class C(P):
    pass

c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()


