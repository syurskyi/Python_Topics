# threading_lock_reacquire.py

import threading

lock = threading.Lock()

print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))

# $ python3 threading_lock_reacquire.py
#
# First try : True
# Second try: False

