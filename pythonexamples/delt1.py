class Test:
    def __init__(self):
        print('Constructor')
    def __del__(self):
        print('Destructor ')
t=Test()
del t
print('End of Application')        