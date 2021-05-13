class Test:
    a=10
    @classmethod
    def m1(cls):
        del Test.a

print(Test.__dict__)        