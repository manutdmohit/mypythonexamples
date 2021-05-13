class A:
    def m1(self):
        print('A class Method')
class B:
    def m1(self):
        print('B class Method')
class C:
    def m1(self):  
        print('C class Method')
class D(A,B):
    def m1(self):
        print('D class Method')
class E(B,C):
    def m1(self):
        print('E class Method')
class F(D,E,C):
    def m1(self):
        print('F class Method')        
f=F()
f.m1()