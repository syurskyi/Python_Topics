# ch16/example3.py

______ th..
____ c__.f.. ______ TPE..
______ ti..
______ matplotlib.pyplot as plt

c_ LockedCounter:
    ___  - (self):
        self.value _ 0
        self.lock _ ?.Lock()

    ___ increment(self, x):
        w__ self.lock:
            new_value _ self.value + x
            t__.s..(0.001) # creating a delay
            self.value _ new_value

    ___ get_value(self):
        w__ self.lock:
            value _ self.value

        r_ value

n_threads _    # list
times _    # list
___ n_workers __ ra..(1, 11):
    n_threads.ap..(n_workers)

    counter _ LockedCounter()

    start _ t__.t__()

    w__ TPE..(max_workers_n_workers) as executor:
        executor.m..(counter.increment, [1 ___ i __ ra..(100 * n_workers)])

    times.ap..(t__.t__() - start)

    print(f'Number of threads: {n_workers}')
    print(f'Final counter: {counter.get_value()}.')
    print(f'Time taken: {times[-1] : .2f} seconds.')
    print('-' * 40)

plt.plot(n_threads, times)
plt.xlabel('Number of threads'); plt.ylabel('Time in seconds')
plt.show()
