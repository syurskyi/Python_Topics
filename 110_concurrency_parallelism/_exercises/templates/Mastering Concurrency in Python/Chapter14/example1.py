# ch14/example1.py

______ th..
______ random
______ ti..

___ update():
    g.. counter

    current_counter _ counter # reading in shared resource
    t__.s..(random.randint(0, 1)) # simulating heavy calculations
    counter _ current_counter + 1 # updating shared resource

counter _ 0

threads _ [?.T..(target_update) ___ i __ ra..(20)]

___ thread __ threads:
    thread.s..
___ thread __ threads:
    thread.j..

print(f'Final counter: {counter}.')
print('Finished.')
