______ _
______ l__

l__.?(?_l__.D..
                    ?_ _threadName)-10s)  _ m.. _,
                    )

___ worker_with(lock):
    with lock:
        l__.d..('Lock acquired via with')
        
___ worker_no_with(lock):
    lock.a..
    ___
        l__.d..('Lock acquired directly')
    ______
        lock.r..

lock = _.?
w = _.? ?_worker_with,  ?_(lock,))
nw = _.? ?_worker_no_with,  ?_(lock,))

w.s..
nw.s..
