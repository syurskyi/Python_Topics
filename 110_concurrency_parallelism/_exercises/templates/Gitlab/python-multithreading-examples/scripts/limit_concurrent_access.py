
______ l__
______ r__
______ _
______ t__

l__.?(?_l__.D..
                    ?_'%(asctime)s (%(threadName)-2s)  _ m.. _,
                    )

c_ ActivePool(object):
    ___ - 
        super(ActivePool, self).- ()
        active   # list
        lock = _.?
    ___ makeActive name):
        with lock:
            active.a.. (name)
            l__.d..('Running: @', active)
    ___ makeInactive name):
        with lock:
            active.remove(name)
            l__.d..('Running: @', active)

___ worker(s, pool):
    l__.d..('Waiting to join the pool')
    with s:
        name = _.c...getName()
        pool.makeActive(name)
        t__.s..(0.1)
        pool.makeInactive(name)

pool = ActivePool()
s = _.Semaphore(2)
___ i __ r.. 4):
    t = _.? ?_worker, ?_s..(i),  ?_(s, pool))
    t.s..
    
