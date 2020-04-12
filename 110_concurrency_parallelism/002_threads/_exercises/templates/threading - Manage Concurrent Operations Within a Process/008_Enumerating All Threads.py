# threading_enumerate.py

import random
import threading
import time
import logging


def worker():
    """thread worker function"""
    pause = random.randint(1, 5) / 10
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(3):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()

# $ python3 threading_enumerate.py
#
# (Thread-1  ) sleeping 0.20
# (Thread-2  ) sleeping 0.30
# (Thread-3  ) sleeping 0.40
# (MainThread) joining Thread-1
# (Thread-1  ) ending
# (MainThread) joining Thread-3
# (Thread-2  ) ending
# (Thread-3  ) ending
# (MainThread) joining Thread-2

