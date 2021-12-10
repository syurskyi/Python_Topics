

______ logging
______ r__
______ _
______ t__


c_ Counter:

    ___ - (self, start=0):

        lock=_.?
        value=start

    ___ increment
        logging.debug('wait  for lock')
        lock.a..

        ___
            logging.debug('Acquire lock')
            value = value+1
        finally:
            lock.r..



___ worker(c):

    ___ i __ r.. 2):

        pause = r__.r__()
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
___ t __ _.e..:
    __ t is n.. main_thread:
        t.j..
logging.debug('Counter: %d', counter.value)

