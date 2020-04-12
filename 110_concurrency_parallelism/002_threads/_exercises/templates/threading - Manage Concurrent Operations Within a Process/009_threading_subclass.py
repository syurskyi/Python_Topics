# threading_subclass.py

import threading
import logging


class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(5):
    t = MyThread()
    t.start()

# $ python3 threading_subclass.py
#
# (Thread-1  ) running
# (Thread-2  ) running
# (Thread-3  ) running
# (Thread-4  ) running
# (Thread-5  ) running

