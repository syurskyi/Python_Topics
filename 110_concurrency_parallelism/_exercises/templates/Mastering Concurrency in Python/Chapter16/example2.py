# ch16/example2.py

______ th..
____ c__.f.. ______ TPE..
______ ti..

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

counter _ LockedCounter()
w__ TPE..(max_workers_3) as executor:
    executor.m..(counter.increment, [1 ___ i __ ra..(300)])

print(f'Final counter: {counter.get_value()}.')
print('Finished.')
