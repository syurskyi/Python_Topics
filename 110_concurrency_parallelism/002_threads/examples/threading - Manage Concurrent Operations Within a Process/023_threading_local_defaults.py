# threading_local_defaults.py

import random
import threading
import logging


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)


def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)


class MyLocal(threading.local):

    def __init__(self, value):
        super().__init__()
        logging.debug('Initializing %r', self)
        self.value = value


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

local_data = MyLocal(1000)
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()

# $ python3 threading_local_defaults.py
#
# (MainThread) Initializing <__main__.MyLocal object at
# 0x101c6c288>
# (MainThread) value=1000
# (Thread-1  ) Initializing <__main__.MyLocal object at
# 0x101c6c288>
# (Thread-1  ) value=1000
# (Thread-1  ) value=18
# (Thread-2  ) Initializing <__main__.MyLocal object at
# 0x101c6c288>
# (Thread-2  ) value=1000
# (Thread-2  ) value=77