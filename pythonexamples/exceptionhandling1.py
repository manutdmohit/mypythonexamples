try:
    print(10/0)
except ZeroDivisionError as msg:
    print('Exception Type:',type(msg))
    print('Exception Type:',msg.__class__)
    print('The Exception class name :',msg.__class__.__name__)
    print('Description of Exception',msg)



