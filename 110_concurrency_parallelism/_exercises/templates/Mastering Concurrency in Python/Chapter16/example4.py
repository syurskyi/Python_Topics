# ch16/example4.py

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

c_ ApproximateCounter:
    ___  - (self, global_counter):
        self.value _ 0
        self.lock _ ?.Lock()
        self.global_counter _ global_counter
        self.threshold _ 10

    ___ increment(self, x):
        w__ self.lock:
            new_value _ self.value + x
            t__.s..(0.001) # creating a delay
            self.value _ new_value

            __ self.value >_ self.threshold:
                self.global_counter.increment(self.value)
                self.value _ 0

    ___ get_value(self):
        w__ self.lock:
            value _ self.value

        r_ value

###########################################################################
# Previous single-lock counter

single_counter_n_threads _    # list
single_counter_times _    # list
___ n_workers __ ra..(1, 11):
    single_counter_n_threads.ap..(n_workers)

    counter _ LockedCounter()

    start _ t__.t__()

    w__ TPE..(max_workers_n_workers) as executor:
        executor.m..(counter.increment, [1 ___ i __ ra..(100 * n_workers)])

    single_counter_times.ap..(t__.t__() - start)

###########################################################################
# New approximate counters

___ thread_increment(counter):
    counter.increment(1)

approx_counter_n_threads _    # list
approx_counter_times _    # list
___ n_workers __ ra..(1, 11):
    approx_counter_n_threads.ap..(n_workers)

    global_counter _ LockedCounter()

    start _ t__.t__()

    local_counters _ [ApproximateCounter(global_counter) ___ i __ ra..(n_workers)]
    w__ TPE..(max_workers_n_workers) as executor:
        ___ i __ ra..(100):
            executor.m..(thread_increment, local_counters)

    approx_counter_times.ap..(t__.t__() - start)

    print(f'Number of threads: {n_workers}')
    print(f'Final counter: {global_counter.get_value()}.')
    print('-' * 40)

###########################################################################
# Plotting

single_counter_line, _ plt.plot(
    single_counter_n_threads,
    single_counter_times,
    c _ 'blue',
    label _ 'Single counter'
)
approx_counter_line, _ plt.plot(
    approx_counter_n_threads,
    approx_counter_times,
    c _ 'red',
    label _ 'Approximate counter'
)
plt.legend(handles_[single_counter_line, approx_counter_line], loc_2)
plt.xlabel('Number of threads'); plt.ylabel('Time in seconds')
plt.show()
