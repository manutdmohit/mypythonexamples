name='durga'
salary=10000
gf='sunny'
print('Hello {}, your salary is {} and your friend {} is waiting.'.format(name,salary,gf))
print('Hello {0}, your salary is {1} and your friend {2} is waiting.'.format(name,salary,gf))
print('Hello {1}, your salary is {2} and your friend {0} is waiting.'.format(name,salary,gf))
print('Hello {n}, your salary is {s} and your friend {g} is waiting.'.format(n=name,s=salary,g=gf))    #keyword
print('Helno {n}, your salary is {s} and your friend {g} is waiting.'.format(s=salary,g=gf,n=name))
