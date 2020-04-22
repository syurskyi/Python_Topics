# ch16/example1.py

____ c__.f.. ______ TPE..
______ ti..

c_ LocklessCounter:
    ___  - (self):
        self.value _ 0

    ___ increment(self, x):
        new_value _ self.value + x
        t__.s..(0.001) # creating a delay
        self.value _ new_value

    ___ get_value(self):
        r_ self.value

counter _ LocklessCounter()
w__ TPE..(max_workers_3) as executor:
    executor.m..(counter.increment, [1 ___ i __ ra..(300)])

print(f'Final counter: {counter.get_value()}.')
print('Finished.')
