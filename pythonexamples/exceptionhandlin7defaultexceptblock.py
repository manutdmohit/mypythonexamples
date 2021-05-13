try:
    x=int(input('Enter First Number:'))
    y=int(input('Enter Second NUmber'))
    print('The Result:',x/y)
except ZeroDivisionError:
    print('Zero Division Error:divide by zero')
except:
    print('Default Except block provide int value')    
