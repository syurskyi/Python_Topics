import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


# Example 2
from time import time
numbers = [2139079, 1214759, 1516637, 1852285]
start = time()
for number in numbers:
    list(factorize(number))
end = time()
print('Took %.3f seconds' % (end - start))


# Example 3
from threading import Thread

class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


# Example 4
start = time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)


# Example 5
for thread in threads:
    thread.join()
end = time()
print('Took %.3f seconds' % (end - start))


# Example 6
import select, socket

# Creating the socket is specifically to support Windows. Windows can't do
# a select call with an empty list.
def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)


# Example 7
start = time()
for _ in range(5):
    slow_systemcall()
end = time()
print('Took %.3f seconds' % (end - start))


# Example 8
start = time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)


# Example 9
def compute_helicopter_location(index):
    pass

for i in range(5):
    compute_helicopter_location(i)
for thread in threads:
    thread.join()
end = time()
print('Took %.3f seconds' % (end - start))
