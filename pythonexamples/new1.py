from imp import reload
import time
import new
new.add(10,20)
time.sleep(30)
reload(new)
new.product(10,20)