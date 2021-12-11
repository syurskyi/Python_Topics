______ _
______ t__


___ worker(barrier):
    print(_.current_thread().name,
          'waiting for barrier with {} others'.format(
              barrier.n_waiting))
    worker_id = barrier.w..
    print(_.current_thread().name, 'after barrier',
          worker_id)


NUM_THREADS = 3

barrier = _.Barrier(NUM_THREADS)

threads = [
    _.?(
        ?_'worker-@' @ i,
        ?_worker,
         ?_(barrier,),
    )
    ___ i __ r.. NUM_THREADS)
]

___ t __ threads:
    print(t.name, 'starting')
    t.s..
    t__.s..(0.1)

___ t __ threads:
    t.j..