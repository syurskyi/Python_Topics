# ch4/example4.py

______ th..

c_ acquire(object):
    ___  - (self, *locks):
        self.locks _ sorted(locks, key_lambda x: id(x))

    ___ __enter__(self):
        ___ lock __ self.locks:
            lock.a..

    ___ __exit__(self, ty, val, tb):
        ___ lock __ reversed(self.locks):
            lock.release()
        r_ F..

# The philosopher thread
___ philosopher(left, right):
    w__ T..:
        w__ acquire(left,right):
             print(f'Philosopher at {?.currentThread()} is eating.')

# The chopsticks
N_FORKS _ 5
forks _ [?.Lock() ___ n __ ra..(N_FORKS)]

# Create all of the philosophers
phils _ [?.T..(
    target_philosopher,
    args_(forks[n], forks[(n + 1) % N_FORKS])
) ___ n __ ra..(N_FORKS)]

# Run all of the philosophers
___ p __ phils:
    p.s..
