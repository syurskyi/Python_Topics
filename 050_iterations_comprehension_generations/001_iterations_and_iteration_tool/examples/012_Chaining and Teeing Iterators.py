# Chaining and Teeing Iterators
# suppose we have some generators producing squares:
# And we want to essentially iterate through all the values as if they were a single iterator.
# In fact, we could even create our own generator function to do this:
# a much simpler way is to use chain in the itertools module:
# As you can see, it simply took our list and handed it back directly - there was nothing else to chain with:
# Instead, we could use unpacking:

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for gen in (l1, l2, l3):
    for item in gen:
        print(item)

def chain_iterables(*iterables):
    for iterable in iterables:
        yield from iterable

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for item in chain_iterables(l1, l2, l3):
    print(item)

from itertools import chain

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for item in chain(l1, l2, l3):
    print(item)

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

lists = [l1, l2, l3]
for item in chain(lists):
    for i in item:
        print(i)

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

lists = [l1, l2, l3]
for item in chain(*lists):
    print(item)

# Chaining and Teeing Iterators
# But, unpacking is not lazy!! Here's a simple example that shows this,
# and why we have to be careful using unpacking if we want to preserve lazy evaluation:
# Instead we can use an alternate "constructor" for chain, that takes a single iterable (of iterables)
# and lazily iterates through the outer iterable as well:
# Note also, that we can easily reproduce the same behavior of either chain quite easily:
# And we can use those just as we saw before with chain and chain.from_iterable:

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

def squares():
    print('yielding 1st item')
    yield (i**2 for i in range(4))
    print('yielding 2nd item')
    yield (i**2 for i in range(4, 8))
    print('yielding 3rd item')
    yield (i**2 for i in range(8, 12))

def read_values(*args):
    print('finised reading args')

read_values(*squares())

c = chain.from_iterable(squares())

for item in c:
    print(item)

def chain_(*args):
    for item in args:
        yield from item

def chain_iter(iterable):
    for item in iterable:
        yield from item

c = chain_(*squares())

c = chain_iter(squares())
for item in c:
    print(item)
