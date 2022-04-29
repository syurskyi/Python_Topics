import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
print('foo bar')


# Example 2
print('%s' % 'foo bar')


# Example 3
print(5)
print('5')


# Example 4
a = '\x07'
print(repr(a))


# Example 5
b = eval(repr(a))
assert a == b


# Example 6
print(repr(5))
print(repr('5'))


# Example 7
print('%r' % 5)
print('%r' % '5')


# Example 8
class OpaqueClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = OpaqueClass(1, 2)
print(obj)


# Example 9
class BetterClass(object):
    def __init__(self, x, y):
        self.x = 1
        self.y = 2
    def __repr__(self):
        return 'BetterClass(%d, %d)' % (self.x, self.y)


# Example 10
obj = BetterClass(1, 2)
print(obj)


# Example 11
obj = OpaqueClass(4, 5)
print(obj.__dict__)
