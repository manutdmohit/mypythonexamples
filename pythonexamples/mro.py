class A:
    def m1(self):
        print('A class Method')
class B(A):
    def m1(self):
        print('B class Method')
class C(A):
    def m1(self):
        print('C class Method')
class D(B,C):
    def m1(self):
        print('D class Method')
d=D()
d.m1()
