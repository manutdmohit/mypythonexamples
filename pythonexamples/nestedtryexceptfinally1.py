try:
    print('Outer try block')
    try:
        print('Inner try block')
        print(10/0)
    except ZeroDivisionError:
        print('Inner except block')
    finally:
        print('Inner finally block') 
except:
    print('outer except block') 
finally:
    print('outer finally block')              
