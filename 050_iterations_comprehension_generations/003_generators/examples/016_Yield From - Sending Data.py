# Yield From - Sending Data
#
# When we use yield from to delegate to a subgenerator, the established communication conduit also carries any data
# sent to the delegator generator.
# Let's write a simple coroutine that will receive string data and print the reversed string to the console:
# We can use this coroutine this way:
# And we can close the generator:

def echo():
    while True:
        received = yield
        print(received[::-1])

e = echo()
next(e)  # prime the coroutine

e.send('stressed')
e.send('tons')
e.close()

# Yield From - Sending Data
# Now let's write a simple delegator generator:
# We can create the delegator generator and prime the delegator:
# Now, calling next on the delegator will establish the connection to the subgenerator and automatically prime
# it as well.
# We can easily see this by doing some inspection:
# We can now send data to the delegator, and it will pass that along to the subgenerator:

def delegator():
    e = echo()
    yield from e

d = delegator()
next(d)

from inspect import getgeneratorstate, getgeneratorlocals
getgeneratorlocals(d)
e = getgeneratorlocals(d)['e']
print(getgeneratorstate(d))
print(getgeneratorstate(e))

# Yield From - Sending Data
# Let's modify our echo coroutine to both receive and yield a result, instead of just printing to the console:
# And we can use delegation as follows:

def echo():
    output = None
    while True:
        received = yield output
        output = received[::-1]

e = echo()
next(e)
e.send('stressed')

def delegator():
    yield from echo()

d = delegator()
next(d)

d.send('stressed')
