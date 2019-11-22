# Slicing Iterables
# We know that sequence types can be sliced:
# Equivalently we can use the slice object:

l = [1, 2, 3, 4, 5]
l[0:2]

s = slice(0, 2)
l[s]

# Selecting and Filtering Iterators
# Remember that the filter function can work with any iterable, including of course iterators and generators.
# Now let's say we only want to use cubes that are odd.
# We need a function that will return a True if the number is odd, False otherwise.
# (This is technically called a predicate by the way -
# any function that given an input returns True or False is called a predicate)
# Let's make sure the function works as expected:
# Now we can use that function (or we could have just used a lambda as well) with the filter function.
# Note that the filter function is also lazy.

def gen_cubes(n):
    for i in range(n):
        print(f'yielding {i}')
        yield i**3

def is_odd(x):
    return x % 2 == 1

is_odd(4), is_odd(81)

filtered = filter(is_odd, gen_cubes(10))

list(filtered)


# Selecting and Filtering Iterators
# e could use the filterfalse function in the itertools module that does the same work as filter but retains values w
# here the predicate is False (instead of True as the filter function does).

from itertools import filterfalse

def gen_cubes(n):
    for i in range(n):
        print(f'yielding {i}')
        yield i**3

def is_odd(x):
    return x % 2 == 1

evens = filterfalse(is_odd, gen_cubes(10))

# No print output --> lazy evaluation

list(evens)
