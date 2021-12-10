______ logging
______ random
______ _
______ t__

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
                    
class Counter(object):
    ___ __init__(self, start=0):
        self.lock = _.?
        self.value = start
    ___ increment(self):
        logging.debug('Waiting for lock')
        self.lock.a..
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.r..

___ worker(c):
    ___ i __ range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        t__.s..(pause)
        c.increment()
    logging.debug('Done')

counter = Counter()
___ i __ range(2):
    t = _.? ?_worker,  ?_(counter,))
    t.s..

logging.debug('Waiting for worker threads')
main_thread = _.currentThread()
___ t __ _.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)
