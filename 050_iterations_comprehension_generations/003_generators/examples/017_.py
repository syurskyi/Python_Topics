# Let's take a look at a more interesting example of yield from.
# Our goal is to flatten a list containing nested lists to any level.
# And of course we can, if we prefer, make a list out of it:

l = [1, 2, [3, 4, [5, 6]], [7, [8, 9, 10]]]

def flatten_gen(curr_item):
    if isinstance(curr_item, list):
        for item in curr_item:
            yield from flatten_gen(item)
    else:
        yield curr_item

for item in flatten_gen(l):
    print(item)

list(flatten_gen(l))

# Our goal is to flatten a list containing nested lists to any level.
# Why are we getting this recursion error?
# That's because strings are iterables too - even a single character string!
# So, two issues: we may not want to treat strings as iterables, and if we do, then we need to be careful with single
# character strings.
# We're going to tweak our is_iterable function, and our flatten generator to handle these two issues:
# Let's just make sure our function works as expected:
# Good, now we can tweak our flatten generator so we can tell it whether to handle strings as iterables or not:

l = [1, 2, [3, 4, [5, 6]], [7, [8, 9, 10]]]

def is_iterable(item, *, str_is_iterable=True):
    try:
        iter(item)
    except:
        return False
    else:
        if isinstance(item, str):
            if str_is_iterable and len(item) > 1:
                return True
            else:
                return False
        else:
            return True

print(is_iterable([1, 2, 3]))
print(is_iterable('abc'))
print(is_iterable('a'))

print(is_iterable([1, 2, 3], str_is_iterable=False))
print(is_iterable('abc', str_is_iterable=False))
print(is_iterable('a', str_is_iterable=False))

def flatten_gen(curr_item, *, str_is_iterable=True):
    if is_iterable(curr_item, str_is_iterable=str_is_iterable):
        for item in curr_item:
            yield from flatten_gen(item, str_is_iterable=str_is_iterable)
    else:
        yield curr_item

llist(flatten_gen(l))
list(flatten_gen(l, str_is_iterable=False))

# we saw we could use yield from recursively. In fact a generator can be both a delegator and a subgenerator.
# Here's a simple example of this:

def coro():
    while True:
        received = yield
        print(received)


def gen1():
    yield from gen2()


def gen2():
    yield from gen3()


def gen3():
    yield from coro()


g = gen1()
next(g)

g.send('hello')
