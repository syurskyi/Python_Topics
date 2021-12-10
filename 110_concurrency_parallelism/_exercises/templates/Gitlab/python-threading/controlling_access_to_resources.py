

______ l__
______ r__
______ _
______ t__


c_ Counter:

    ___ -  start=0):

        lock=_.?
        value=start

    ___ increment
        l__.d..('wait  for lock')
        lock.a..

        ___
            l__.d..('Acquire lock')
            value = value+1
        ______
            lock.r..



___ worker(c):

    ___ i __ r.. 2):

        pause = r__.r__()
        l__.d..('sleeping %0.002f',pause)
        t__.s..(pause)
        c.i..

    l__.d..('Done')


l__.?(
    ?_l__.D..
    ?_ _threadName)-10s)  _ m.. _,
)


counter = Counter()
___ i __ r.. 2):
    t = _.? ?_worker,  ?_(counter,))
    t.s..

l__.d..('Waiting for worker threads')
main_thread = _.main_thread()
___ t __ _.e..:
    __ t __ n.. main_thread:
        t.j..
l__.d..('Counter: %d', counter.value)

