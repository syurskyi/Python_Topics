# Generator States
# We create an generator object by calling the generator function:
# At this point the generator object is created, but we have not actually started running it. To do so, we call next(),
# which then starts running the function body until the first yield is encountered:
#
# Now the generator is suspended, waiting for us to call next again:
#
# Every time we call next, the generator function runs, or is in a running state until the next yield is encountered,
# or no more results are yielded and the function actually returns:

def gen(s):
    for c in s:
        yield c

g = gen('abc')

next(g)

next(g)

next(g)

# Generator States
#
# We can actually request the state of a generator programmatically by using the inspect module's
# getgeneratorstate() function:
#
# We can start running the generator by calling next:
#
# And the state is now:
# Once we exhaust the generator:
# The generator is now in a closed state:

from inspect import getgeneratorstate
g = gen('abc')
getgeneratorstate(g)

next(g)

getgeneratorstate(g)

next(g), next(g), next(g)

# Generator States
#
# Now we haven't seen the running state - to do that we just need to print the state from inside the generator -
# but to do that we need to have a reference to the generator object itself. This is not that easy to do,
# so I'm going to cheat and assume that the generator object will be referenced by a global variable global_gen:

def gen(s):
    for c in s:
        print(getgeneratorstate(global_gen))
        yield c

global_gen = gen('abc')

next(global_gen)

# Generator States
#
# Finally it is really important to understand that when a yield is encountered,
# the generator is suspended exactly at that point, but not before it has evaluated the expression to the right
# of the yield statement so it can produce that value in the return value of the next() function.
#
# As you can see square(i) was evaluated, then the value was yielded, and the genrator was suspended exactly at
# the point the yield statement was encountered:
#
# As you can see, only now does the right after yield string get printed from our generator.

def square(i):
    print(f'squaring {i}')
    return i ** 2

def squares(n):
    for i in range(n):
        yield square(i)
        print ('right after yield')

sq = squares(5)
next(sq)

next(sq)
