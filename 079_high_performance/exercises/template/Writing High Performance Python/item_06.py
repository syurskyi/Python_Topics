import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)


# Example 2
x = b'mongoose'
y = x[::-1]
print(y)


# Example 3
try:
    w = '謝謝'
    x = w.encode('utf-8')
    y = x[::-1]
    z = y.decode('utf-8')
except:
    logging.exception('Expected')
else:
    assert False


# Example 4
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[::2]   # ['a', 'c', 'e', 'g']
a[::-2]  # ['h', 'f', 'd', 'b']


# Example 5
a[2::2]     # ['c', 'e', 'g']
a[-2::-2]   # ['g', 'e', 'c', 'a']
a[-2:2:-2]  # ['g', 'e']
a[2:2:-2]   # []


# Example 6
b = a[::2]   # ['a', 'c', 'e', 'g']
c = b[1:-1]  # ['c', 'e']
print(a)
print(b)
print(c)
