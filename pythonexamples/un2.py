from imp import reload
import time
import un
un.add(10,20)
print('Entering into sleeping state')
time.sleep(30)
reload(un)
print('Just wakeup...trying to use module again')
import un
un.product(10,20)