______ _
______ logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

___ worker_with(lock):
    with lock:
        logging.debug('Lock acquired via with')
        
___ worker_no_with(lock):
    lock.a..
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.r..

lock = _.?
w = _.? ?_worker_with,  ?_(lock,))
nw = _.? ?_worker_no_with,  ?_(lock,))

w.s..
nw.s..
