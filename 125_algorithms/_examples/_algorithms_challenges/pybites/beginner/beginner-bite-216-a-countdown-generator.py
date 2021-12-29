"""
Write a simple generator that counts from 100 to 1. It can just return the ints one by one, no fancy formatting,
just focus on the basic mechanics of generators. Remember that going beyond 1 it would trigger a StopIteration exception.

Here is how it works:

>>> from countdown import countdown
>>> cd = countdown()
>>> next(cd)
100
>>> next(cd)
99
>>> next(cd)
98
>>> next(cd)
97
...
... 95 calls more
...
>>> next(cd)
1
>>> next(cd)
Traceback (most recent call last):
  File "", line 1, in
StopIteration
Good luck, have fun and keep it Python!

"""

def countdown():
    for i in range(100, 0, -1):
        yield i


for x in countdown():
    print(x)