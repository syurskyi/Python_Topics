
threading_semaphore.py

import logging
import random
import threading
import time


class ActivePool:

    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s', self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)


def worker(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.current_thread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

pool = ActivePool()
s = threading.Semaphore(2)
for i in range(4):
    t = threading.Thread(
        target=worker,
        name=str(i),
        args=(s, pool),
    )
    t.start()

# $ python3 threading_semaphore.py
#
# 2016-07-10 10:45:29,398 (0 ) Waiting to join the pool
# 2016-07-10 10:45:29,398 (0 ) Running: ['0']
# 2016-07-10 10:45:29,399 (1 ) Waiting to join the pool
# 2016-07-10 10:45:29,399 (1 ) Running: ['0', '1']
# 2016-07-10 10:45:29,399 (2 ) Waiting to join the pool
# 2016-07-10 10:45:29,399 (3 ) Waiting to join the pool
# 2016-07-10 10:45:29,501 (1 ) Running: ['0']
# 2016-07-10 10:45:29,501 (0 ) Running: []
# 2016-07-10 10:45:29,502 (3 ) Running: ['3']
# 2016-07-10 10:45:29,502 (2 ) Running: ['3', '2']
# 2016-07-10 10:45:29,607 (3 ) Running: ['2']
# 2016-07-10 10:45:29,608 (2 ) Running: []
