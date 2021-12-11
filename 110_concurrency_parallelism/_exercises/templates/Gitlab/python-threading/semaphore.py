______ l__
______ r__
______ _
______ t__


c_ ActivePool:

    ___ - 
        s__(ActivePool, .- ()
        active   # list
        lock = _.?

    ___ makeActive name):
        w__ lock:
            active.a.. (name)
            l__.d..('Running: @', active)

    ___ makeInactive name):
        w__ lock:
            active.r..(name)
            l__.d..('Running: @', active)


___ worker(s, pool):
    l__.d..('Waiting to join the pool')
    w__ s:
        name = _.current_thread().g..
        pool.makeActive(name)
        t__.s..(0.1)
        pool.makeInactive(name)


l__.?(
    ?_l__.D..
    ?_'%(asctime)s (%(threadName)-2s)  _ m.. _,
)

pool = ActivePool()
s = _.S..(2)
___ i __ r.. 4):
    t = _.?(
        ?_worker,
        ?_s..(i),
         ?_(s, pool),
    )
    t.s..