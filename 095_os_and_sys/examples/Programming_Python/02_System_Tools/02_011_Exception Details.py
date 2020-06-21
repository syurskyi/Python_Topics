import sys
try:
    raise IndexError
except:
    print(sys.exc_info())

# (<class 'IndexError'>, IndexError(), <traceback object at 0x019B8288>)

import traceback, sys

def grail(x):
    raise TypeError('already got one')

try:
    grail('arthur')
except:
    exc_info = sys.exc_info()
    print(exc_info[0])
    print(exc_info[1])
    traceback.print_tb(exc_info[2])

# <class 'TypeError'>
# already got one
# File "<stdin>", line 2, in <module>
# File "<stdin>", line 2, in grail