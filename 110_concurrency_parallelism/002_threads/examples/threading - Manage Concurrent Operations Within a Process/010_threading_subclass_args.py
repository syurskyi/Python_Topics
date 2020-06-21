# threading_subclass_args.py

import threading
import logging


class MyThreadWithArgs(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('running with %s and %s',
                      self.args, self.kwargs)


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(5):
    t = MyThreadWithArgs(args=(i,), kwargs={'a': 'A', 'b': 'B'})
    t.start()

# $ python3 threading_subclass_args.py
#
# (Thread-1  ) running with (0,) and {'b': 'B', 'a': 'A'}
# (Thread-2  ) running with (1,) and {'b': 'B', 'a': 'A'}
# (Thread-3  ) running with (2,) and {'b': 'B', 'a': 'A'}
# (Thread-4  ) running with (3,) and {'b': 'B', 'a': 'A'}
# (Thread-5  ) running with (4,) and {'b': 'B', 'a': 'A'}



