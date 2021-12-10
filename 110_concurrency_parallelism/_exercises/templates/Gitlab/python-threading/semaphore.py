______ logging
______ r__
______ _
______ t__


c_ ActivePool:

    ___ - 
        super(ActivePool, self).- ()
        active   # list
        lock = _.?

    ___ makeActive(self, name):
        with lock:
            active.a.. (name)
            logging.debug('Running: @', active)

    ___ makeInactive(self, name):
        with lock:
            active.remove(name)
            logging.debug('Running: @', active)


___ worker(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = _.current_thread().getName()
        pool.makeActive(name)
        t__.s..(0.1)
        pool.makeInactive(name)


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

pool = ActivePool()
s = _.Semaphore(2)
___ i __ r.. 4):
    t = _.?(
        target=worker,
        name=s..(i),
         ?_(s, pool),
    )
    t.s..