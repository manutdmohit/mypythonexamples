try:
    x=int(input('Enter First Number:'))
    y=int(input('Enter Second Number:'))
    print('The Result:',x/y)
except(ZeroDivisionError,ValueError)as msg:
    print('Exception Name:',msg.__class__.__name__)
    print('Description of exception',msg)
    print('Please provide valid input only')    
