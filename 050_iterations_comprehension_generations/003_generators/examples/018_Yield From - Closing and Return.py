# Yield From - Closing and Return
# Just as we can send next and send through a delegator, we can also send close.
# How does this affect the delegator and the subgenerator?
# At this point, both the delegator and the subgenerator are primed and suspended:
# We can send data to the delegator:
# We can even send data directly to the subgenerator since we now have a handle on it:
# In fact, we can close it too:
# So, what is the state of the delegator now?
# But the subgenerator closed, so let's see what happens when we call next on d:
# As you can see, the generator code resume right after the yield from,
# and we can do this one more time to close the delegator:

def subgen():
    try:
        while True:
            received = yield
            print(received)
    finally:
        print('subgen: closing...')

def delegator():
    s = subgen()
    yield from s
    yield 'delegator: subgen closed'
    print('delegator: closing...')

d = delegator()
next(d)

from inspect import getgeneratorstate, getgeneratorlocals

getgeneratorlocals(d)

s = getgeneratorlocals(d)['s']
print(getgeneratorstate(d))
print(getgeneratorstate(s))

d.send('hello')
s.send('python')
s.close()

getgeneratorstate(d)

next(d)

# Yield From - Closing and Return
# so this is what happens when the subgenerator closes (directly or indirectly) - the delegator simply resumes running
# right after the yield from when we call next.
# But what happens if we close the delegator instead of just closing the subgenerator?
# As you can see the subgenerator also closed. Is the delegator closed too?

d = delegator()
next(d)
s = getgeneratorlocals(d)['s']
print(getgeneratorstate(d))
print(getgeneratorstate(s))

d.close()

print(getgeneratorstate(d))
print(getgeneratorstate(s))

# Yield From - Closing and Return
# Yes. So closing the delegator will close not only the delegator itself,
# but also close the currently active subgenerator (if any).
# We should notice that when we closed the subgenerator directly no apparent exception was raised in our context.
# What happens if the subgenerator returns something when it closes?
# Hmmm, the StopIteration exception was silenced. Let's do this a different way,
# since we know the StopIteration exception should contain the return value:

def subgen():
    try:
        while True:
            received = yield
            print(received)
    finally:
        print('subgen: closing...')
        return 'subgen: return value'

s = subgen()
next(s)
s.send('hello')
s.close()
s = subgen()
next(s)
s.send('hello')
s.throw(GeneratorExit, 'force exit')

# Yield From - Closing and Return
# OK, so now we can see that the StopIteration exception contains the return value.
# The yield from actually captures that value as it's return value - in other words yield from is not just a statement,
# it is in fact, like yield, also an expression.
# Let's see how that works:
# As you can see the return value of the subgenerator ended up as the result of the yield from expression.

def subgen():
    try:
        yield 1
        yield 2
    finally:
        print('subgen: closing...')
        return 100

def delegator():
    s = subgen()
    result = yield from s
    print('subgen returned:', result)
    yield 'delegator suspended'
    print('delegator closing')

d = delegator()
next(d)
next(d)
next(d)
