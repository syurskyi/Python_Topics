# You're using Python 2.x, which has used .next() since forever and still does so - only Python 3 renamed that method ' \
# to .__next__(). Python 2 and 3 aren't compatible. If you're reading a 3.x book, use Python 3.x yourself, and vice versa.
#
# For Python 2.x, you can change __next__() to next()

from __future__ import print_function
### file: iters.py

class Squares:
    def __init__(self, start, stop):    # Save state when created
        self.value = start - 1
        self.stop = stop
    def __iter__(self):                 # Get iterator object on iter()
        return self
    def __next__(self):                 # Return a square on each iteration
        if self.value == self.stop:     # Also called by next() built-in
            raise StopIteration
        self.value += 1
        return self.value ** 2

print('#' * 23 + 'for calls iter(), which calls __iter__()')
# from iters import Squares
for i in Squares(1, 5):             # for calls iter(), which calls __iter__()
    print(i, end=' ')               # Each iteration calls __next__()

print('#' * 23 + 'Iterate manually: what loops do')
X = Squares(1, 5)                   # Iterate manually: what loops do
I = iter(X)                         # iter() calls __iter__
next(I)                             # next() calls __next__

next(I)

next(I)

# next(I)                             # Can catch this in try statement
# # StopIteration
#
X = Squares(1, 5)
# X[1]
# # AttributeError: Squares instance has no attribute '__getitem__'
#
print('#' * 23 + 'Exhausts items')
X = Squares(1, 5)
print([n for n in X])                # Exhausts items
#
print([n for n in X])                # Now it's empty

print('#' * 23 + 'Make a new iterator object')
print([n for n in Squares(1, 5)])    # Make a new iterator object
#
print(list(Squares(1, 3)))
#
#
print('#' * 23)
print('#' * 23)

def gsquares(start, stop):
    for i in range(start, stop+1):
        yield i ** 2
#
for i in gsquares(1, 5):
    print(i, end=' ')
#
print('#' * 23)
print('#' * 23)
print([x ** 2 for x in range(1, 6)])
#

print('#' * 23)
print('#' * 23)
S = 'ace'
for x in S:
    for y in S:
        print(x + y, end=' ')
#
# ### file: skipper.py
#
class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped                    # Iterator state information
        self.offset  = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):      # Terminate iterations
            raise StopIteration
        else:
            item = self.wrapped[self.offset]      # else return and skip
            self.offset += 2
            return item

class SkipObject:
    def __init__(self, wrapped):                  # Save item to be used
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)         # New iterator each time

if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)                   # Make container object
    I = iter(skipper)                             # Make an iterator on it
    print(next(I), next(I), next(I))              # Visit offsets 0, 2, 4
#
    for x in skipper:               # for calls __iter__ automatically
        for y in skipper:           # Nested fors call __iter__ again each time
            print(x + y, end=' ')   # Each iterator has its own state, offset
#
#
print('#' * 23)
print('#' * 23)
print('#' * 23)

S = 'abcdef'
for x in S[::2]:
    for y in S[::2]:            # New objects on each iteration
        print(x + y, end=' ')

print('#' * 23)
print('#' * 23)

S = 'abcdef'
S = S[::2]
print(S)
print('#' * 23)

for x in S:
    for y in S:                 # Same object, new iterators
        print(x + y, end=' ')

