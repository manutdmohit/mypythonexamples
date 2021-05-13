class Test:
    a=10
    def __init__(self):
        Test.a=20
    def m1(self):
        Test.a=30
    @classmethod
    def m2(cls):
        cls.a=40
        Test.a=50
    @staticmethod
    def m3():
        Test.a=60           
t=Test()
t.m1()
t.m2()
t.m3()        
print(Test.a)       