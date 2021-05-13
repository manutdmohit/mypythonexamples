class P:
    a=888
    def __init__(self):
        self.b=999

class C(P):
    def m1(self):
        print(self.a)
        print(self.b)
        print(super().a)

c=C()
c.m1()