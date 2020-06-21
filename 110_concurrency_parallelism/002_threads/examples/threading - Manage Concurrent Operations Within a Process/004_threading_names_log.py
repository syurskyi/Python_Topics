# threading_names_log.py

import logging
import threading
import time


def worker():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def my_service():
    logging.debug('Starting')
    time.sleep(0.3)
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)  # use default name

w.start()
w2.start()
t.start()

# $ python3 threading_names_log.py
#
# [DEBUG] (worker    ) Starting
# [DEBUG] (Thread-1  ) Starting
# [DEBUG] (my_service) Starting
# [DEBUG] (worker    ) Exiting
# [DEBUG] (Thread-1  ) Exiting
# [DEBUG] (my_service) Exiting
