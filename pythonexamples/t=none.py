class Test:
    def __init__(self):
        print('Constructor')
    def __del__(self):
        print('Destructor ')
t=Test()
t=None
print('End of Application')        