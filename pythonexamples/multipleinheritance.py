class P1:
    def m1(self):
        print('Parent1 Method')
class P2:
    def m2(self):
        print('Parent2 Method')
class C(P1,P2):
    def m3(self):
        print('Child Method')

c=C()
c.m1()
c.m2()
c.m3()
