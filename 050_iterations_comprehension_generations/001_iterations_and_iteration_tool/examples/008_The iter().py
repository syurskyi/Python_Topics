# The iter() Function
# As we have seen before, the iter() function is used to request an iterator object from an iterable
# And we can use that iterator to iterate the collection by calling next() until a StopIteration exception is raised.

l = [1, 2, 3, 4]
l_iter = iter(l)
type(l_iter)
next(l_iter)
next(l_iter)

# The iter() Function
# class Squares with __getitem__

class Squares:
    def __init__(self, n):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self, i):
        if i >= self._n:
            raise IndexError
        else:
            return i ** 2


for i in sq:
    print(i)

sq_iter = iter(sq)
type(sq_iter)
'__next__' in dir(sq_iter)


# How to test if an object is iterable
# Basically an object is iterable if it:
#     implements the iterable protocol (__iter__ that returns an iterator)
#     implements the sequence protocol (__getitem__, and __len__) - although __len__ is not required for iteration
#  the best way, if you have some need to detect if something is iterable or not, is the following:

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

is_iterable(SimpleIter())
is_iterable(Squares(5))

# In this example we are going to create a counter function (using a closure) - it's a pretty simplistic function -
# counter() will return a closure that we can then call to increment an internal counter by 1 every time it is called:

def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i

    return inc


cnt = counter()
cnt()
cnt()

# you may want to iterater through random numbers until a specific random number is generated:

import random
random.seed(0)
for i in range(10):
    print(i, random.randint(0, 10))

random_iterator = iter(lambda : random.randint(0, 10), 8)

random.seed(0)

for num in random_iterator:
    print(num)

#  try a countdown example like the one we discussed in the lecture.
def countdown(start=10):
    def run():
        nonlocal start
        start -= 1
        return start
    return run

takeoff = countdown(10)
for _ in range(15):
    print(takeoff())

takeoff  = countdown(10)
takeoff_iter = iter(takeoff, -1)
for val in takeoff_iter:
    print(val)
