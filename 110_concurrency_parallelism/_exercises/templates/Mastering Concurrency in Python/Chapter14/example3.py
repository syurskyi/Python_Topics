# ch14/example3.py

______ th..
______ random; random.seed(0)
______ ti..

___ update(pause_period):
    g.. counter

    w__ count_lock:
        current_counter _ counter # reading in shared resource
        t__.s..(pause_period) # simulating heavy calculations
        counter _ current_counter + 1 # updating shared resource

pause_periods _ [random.randint(0, 1) ___ i __ ra..(20)]

###########################################################################

counter _ 0
count_lock _ ?.Lock()

start _ t__.perf_counter()
___ i __ ra..(20):
    update(pause_periods[i])

print('--Sequential version--')
print(f'Final counter: {counter}.')
print(f'Took {t__.perf_counter() - start : .2f} seconds.')

###########################################################################

counter _ 0

threads _ [?.T..(target_update, args_(pause_periods[i],)) ___ i __ ra..(20)]

start _ t__.perf_counter()
___ thread __ threads:
    thread.s..
___ thread __ threads:
    thread.j..

print('--Concurrent version--')
print(f'Final counter: {counter}.')
print(f'Took {t__.perf_counter() - start : .2f} seconds.')

###########################################################################

print('Finished.')
