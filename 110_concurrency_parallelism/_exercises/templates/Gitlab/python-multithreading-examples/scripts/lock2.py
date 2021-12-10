#!/usr/bin/python


______ l__
______ _
______ t__

l__.?(?_l__.D..
                    ?_ _threadName)-10s)  _ m.. _,
                    )
                    
___ lock_holder(lock):
    l__.d..('Starting')
    w___ True:
        lock.a..
        ___
            l__.d..('Holding')
            t__.s..(0.5)
        ______
            l__.d..('Not holding')
            lock.r..
        t__.s..(0.5)
    r_
                    
___ worker(lock):
    l__.d..('Starting')
    num_tries = 0
    num_acquires = 0
    w___ num_acquires < 3:
        t__.s..(0.5)
        l__.d..('Trying to acquire')
        have_it = lock.acquire(0)
        ___
            num_tries += 1
            __ have_it:
                l__.d..('Iteration %d: Acquired',  num_tries)
                num_acquires += 1
            else:
                l__.d..('Iteration %d: Not acquired', num_tries)
        ______
            __ have_it:
                lock.r..
    l__.d..('Done after %d iterations', num_tries)


lock = _.?

holder = _.? ?_lock_holder,  ?_(lock,), ?_'LockHolder')
holder.setDaemon(True)
holder.s..

worker = _.? ?_worker,  ?_(lock,), ?_'Worker')
worker.s..
