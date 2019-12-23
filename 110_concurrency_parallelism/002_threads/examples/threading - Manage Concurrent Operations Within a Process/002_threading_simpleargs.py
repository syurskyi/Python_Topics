# threading_simpleargs.py

import threading


def worker(num):
    """thread worker function"""
    print('Worker: %s' % num)


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# $ python3 threading_simpleargs.py
#
# Worker: 0
# Worker: 1
# Worker: 2
# Worker: 3
# Worker: 4



