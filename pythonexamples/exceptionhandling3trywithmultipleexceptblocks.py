try:
    x=int(input('Enter First Number:'))
    y=int(input('Enter Second Number:'))
    print('The result:',x/y)
except ZeroDivisionError:
    print('cannot divide with zero')
except ValueError:
    print('please provide int values only')
