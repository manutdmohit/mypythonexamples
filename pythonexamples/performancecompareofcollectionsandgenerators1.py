import random
import time
names=['sunny','bunny','chinny','vinny']
subjects=['python','java','javascript','datascience']
def student_list(num):
	for i in range(num):
		student={'id':i,'name':random.choice(names),'subject':random.choice(subjects)}
		yield student
t1=time.clock()
g=student_generator(10000)
t2=time.clock()
print('Time required to prepare student list:',t2-t1)

