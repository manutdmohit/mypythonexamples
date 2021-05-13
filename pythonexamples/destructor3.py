import time
class Test:
    def __init__(self):
        print('Constructor Execution...')
    def __del__(self):
        print('Destructor Execution')
l=[Test(),Test(),Test()]
print('Making list object eligible for GC...')
del l
time.sleep(10)
print('End of application')        