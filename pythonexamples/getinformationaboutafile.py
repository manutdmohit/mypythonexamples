import os
from datetime import *
statistics=os.stat('00.py')
print('File Size in Bytes:',statistics.st_size)
print('Last Modified Time:',datetime.fromtimestamp(statistics.st_mtime))

