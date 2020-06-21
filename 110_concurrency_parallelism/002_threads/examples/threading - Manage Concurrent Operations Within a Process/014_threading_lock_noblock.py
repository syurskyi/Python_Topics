# threading_lock_noblock.py

import logging
import threading
import time


def lock_holder(lock):
    logging.debug('Starting')
    while True:
        lock.a..
        try:
            logging.debug('Holding')
            time.sleep(0.5)
        finally:
            logging.debug('Not holding')
            lock.release()
        time.sleep(0.5)


def worker(lock):
    logging.debug('Starting')
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug('Trying to acquire')
        have_it = lock.acquire(0)
        try:
            num_tries += 1
            if have_it:
                logging.debug('Iteration %d: Acquired',
                              num_tries)
                num_acquires += 1
            else:
                logging.debug('Iteration %d: Not acquired',
                              num_tries)
        finally:
            if have_it:
                lock.release()
    logging.debug('Done after %d iterations', num_tries)


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

lock = threading.Lock()

holder = threading.Thread(
    target=lock_holder,
    args=(lock,),
    name='LockHolder',
    daemon=True,
)
holder.start()

worker = threading.Thread(
    target=worker,
    args=(lock,),
    name='Worker',
)
worker.start()

# $ python3 threading_lock_noblock.py
#
# (LockHolder) Starting
# (LockHolder) Holding
# (Worker    ) Starting
# (LockHolder) Not holding
# (Worker    ) Trying to acquire
# (Worker    ) Iteration 1: Acquired
# (LockHolder) Holding
# (Worker    ) Trying to acquire
# (Worker    ) Iteration 2: Not acquired
# (LockHolder) Not holding
# (Worker    ) Trying to acquire
# (Worker    ) Iteration 3: Acquired
# (LockHolder) Holding
# (Worker    ) Trying to acquire
# (Worker    ) Iteration 4: Not acquired
# (LockHolder) Not holding
# (Worker    ) Trying to acquire
# (Worker    ) Iteration 5: Acquired
# (Worker    ) Done after 5 iterations
