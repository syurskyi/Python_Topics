import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


# Example 2
def worker(sensor_index, how_many, counter):
    # I have a barrier in here so the workers synchronize
    # when they start counting, otherwise it's hard to get a race
    # because the overhead of starting a thread is high.
    BARRIER.wait()
    for _ in range(how_many):
        # Read from the sensor
        counter.increment(1)


# Example 3
from threading import Barrier, Thread
BARRIER = Barrier(5)
def run_threads(func, how_many, counter):
    threads = []
    for i in range(5):
        args = (i, how_many, counter)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


# Example 4
how_many = 10**5
counter = Counter()
run_threads(worker, how_many, counter)
print('Counter should be %d, found %d' %
      (5 * how_many, counter.count))


# Example 5
offset = 5
counter.count += offset


# Example 6
value = getattr(counter, 'count')
result = value + offset
setattr(counter, 'count', result)


# Example 7
# Running in Thread A
value_a = getattr(counter, 'count')
# Context switch to Thread B
value_b = getattr(counter, 'count')
result_b = value_b + 1
setattr(counter, 'count', result_b)
# Context switch back to Thread A
result_a = value_a + 1
setattr(counter, 'count', result_a)


# Example 8
from threading import Lock

class LockingCounter(object):
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


# Example 9
BARRIER = Barrier(5)
counter = LockingCounter()
run_threads(worker, how_many, counter)
print('Counter should be %d, found %d' %
      (5 * how_many, counter.count))
