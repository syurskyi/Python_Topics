# Infinite Iterators
# The count function is similar to range, except it does not have a stop value. It has both a start and a step:
#
# Unlike the range function, whose arguments must always be integers, count works with floats as well:
#
# In fact, we can even use other data types as well:
#
# We can even use Decimal numbers:

from itertools import count
g = count(10)
list(islice(g, 5))
g = count(10, step=2)
list(islice(g, 5))

g = count(10.5, 0.5)
list(islice(g, 5))

g = count(1+1j, 1+2j)
list(islice(g, 5))

from decimal import Decimal
g = count(Decimal('0.0'), Decimal('0.1'))
list(islice(g, 5))

# Infinite Iterators
# cycle is used to repeatedly loop over an iterable:
#
# One thing to note is that this works even if the argument is an iterator
# (i.e. gets exhausted after the first complete iteration over it)!
#
# As expected, cols was exhausted after the first iteration.
# Now let's see how cycle behaves:
#
# As you can see, cycle iterated over the elements of iterator, and continued the iteration even though the first run
# through the iterator technically exhausted it.

g = cycle(('red', 'green', 'blue'))
list(islice(g, 8))

def colors():
    yield 'red'
    yield 'green'
    yield 'blue'

cols = colors()
list(cols)
list(cols)

cols = colors()
g = cycle(cols)
list(islice(g, 10))

# Infinite Iterators
# The repeat function is used to create an iterator that just returns the same value again and again.
# By default it is infinite, but a count can be specified optionally:
#
# And we also optionally specify a count to make the iterator finite:
#
# The important thing to note as well, is that the "value" that is returned is the same object every time!

g = repeat('Python')
for _ in range(5):
    print(next(g))

g = repeat('Python', 4)
list(g)

l = [1, 2, 3]
result = list(repeat(l, 3))
result

l is result[0], l is result[1], l is result[2]

# Infinite Iterators
# repeat
#
# If you want to end up with three separate copies of your argument, then you'll need to use a copy mechanism
# (either shallow or deep depending on your needs).
#
# This is easily done using a comprehension expression:

l = [1, 2, 3]
result = [item[:] for item in repeat(l, 3)]
l is result[0], l is result[1], l is result[2]
result[0][0] = 100
result
