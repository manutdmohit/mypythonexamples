class P:
    def __init__(self):
        print('PC')
    def m1(self):
        print('PIM')
    @classmethod
    def m2(cls):
        print('PCM')
    @staticmethod
    def m3():
        print('PSM')

class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    @classmethod
    def m2(cls):
        super(C,cls).__init__(cls)
        super(C,cls).m1(cls)
        super().m2()
        super().m3()
    @staticmethod
    def m3():
         super(C,C).m2()
         super(C,C).m3()  

C.m3()       
