try:
    print('try')
    print(10/0)
except ValueError:
    print('except')
finally:
    print('finally')        