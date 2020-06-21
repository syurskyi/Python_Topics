# threading_simple.py

import threading


def worker():
    """thread worker function"""
    print('Worker')


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# $ python3 threading_simple.py
#
# Worker
# Worker
# Worker
# Worker
# Worker
