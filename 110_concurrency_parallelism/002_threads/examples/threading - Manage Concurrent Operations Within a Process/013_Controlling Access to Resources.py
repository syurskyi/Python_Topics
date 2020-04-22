# threading_lock.py

import logging
import random
import threading
import time


class Counter:

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.a..
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)

# $ python3 threading_lock.py
#
# (Thread-1  ) Sleeping 0.18
# (Thread-2  ) Sleeping 0.93
# (MainThread) Waiting for worker threads
# (Thread-1  ) Waiting for lock
# (Thread-1  ) Acquired lock
# (Thread-1  ) Sleeping 0.11
# (Thread-1  ) Waiting for lock
# (Thread-1  ) Acquired lock
# (Thread-1  ) Done
# (Thread-2  ) Waiting for lock
# (Thread-2  ) Acquired lock
# (Thread-2  ) Sleeping 0.81
# (Thread-2  ) Waiting for lock
# (Thread-2  ) Acquired lock
# (Thread-2  ) Done
# (MainThread) Counter: 4