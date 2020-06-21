# threading_rlock.py

import threading

lock = threading.RLock()

print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))

# $ python3 threading_rlock.py
#
# First try : True
# Second try: True

