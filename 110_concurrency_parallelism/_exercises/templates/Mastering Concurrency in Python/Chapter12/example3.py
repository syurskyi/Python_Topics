# ch12/example3.py

______ th..

# The philosopher thread
___ philosopher(left, right):
    w__ T..:
        w__ left:
             w__ right:
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
