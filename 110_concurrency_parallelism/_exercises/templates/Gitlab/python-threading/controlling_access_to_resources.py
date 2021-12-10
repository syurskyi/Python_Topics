

______ logging
______ random
______ _
______ t__


class Counter:

    ___ __init__(self, start=0):

        self.lock=_.?
        self.value=start

    ___ increment(self):
        logging.debug('wait  for lock')
        self.lock.a..

        try:
            logging.debug('Acquire lock')
            self.value = self.value+1
        finally:
            self.lock.r..



___ worker(c):

    ___ i __ r.. 2):

        pause = random.random()
        logging.debug('sleeping %0.002f',pause)
        t__.s..(pause)
        c.increment()

    logging.debug('Done')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)


counter = Counter()
___ i __ r.. 2):
    t = _.? ?_worker,  ?_(counter,))
    t.s..

logging.debug('Waiting for worker threads')
main_thread = _.main_thread()
___ t __ _.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)

