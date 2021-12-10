#!/usr/bin/python


______ logging
______ _
______ t__

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
                    
___ lock_holder(lock):
    logging.debug('Starting')
    w___ True:
        lock.a..
        try:
            logging.debug('Holding')
            t__.s..(0.5)
        finally:
            logging.debug('Not holding')
            lock.r..
        t__.s..(0.5)
    return
                    
___ worker(lock):
    logging.debug('Starting')
    num_tries = 0
    num_acquires = 0
    w___ num_acquires < 3:
        t__.s..(0.5)
        logging.debug('Trying to acquire')
        have_it = lock.acquire(0)
        try:
            num_tries += 1
            if have_it:
                logging.debug('Iteration %d: Acquired',  num_tries)
                num_acquires += 1
            else:
                logging.debug('Iteration %d: Not acquired', num_tries)
        finally:
            if have_it:
                lock.r..
    logging.debug('Done after %d iterations', num_tries)


lock = _.?

holder = _.? ?_lock_holder,  ?_(lock,), name='LockHolder')
holder.setDaemon(True)
holder.s..

worker = _.? ?_worker,  ?_(lock,), name='Worker')
worker.s..
