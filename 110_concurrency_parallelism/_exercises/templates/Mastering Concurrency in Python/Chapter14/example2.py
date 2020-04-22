# ch14/example2.py

______ th..
______ random
______ ti..

___ update():
    g.. counter

    w__ count_lock:
        current_counter _ counter # reading in shared resource
        t__.s..(random.randint(0, 1)) # simulating heavy calculations
        counter _ current_counter + 1

counter _ 0
count_lock _ ?.Lock()

threads _ [?.T..(target_update) ___ i __ ra..(20)]

___ thread __ threads:
    thread.s..
___ thread __ threads:
    thread.j..

print(f'Final counter: {counter}.')
print('Finished.')
