
______ logging
______ random
______ _
______ t__

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )

class ActivePool(object):
    ___ __init__(self):
        super(ActivePool, self).__init__()
        self.active   # list
        self.lock = _.?
    ___ makeActive(self, name):
        with self.lock:
            self.active.a.. (name)
            logging.debug('Running: @', self.active)
    ___ makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: @', self.active)

___ worker(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = _.currentThread().getName()
        pool.makeActive(name)
        t__.s..(0.1)
        pool.makeInactive(name)

pool = ActivePool()
s = _.Semaphore(2)
___ i __ r.. 4):
    t = _.? ?_worker, name=s..(i),  ?_(s, pool))
    t.s..
    
