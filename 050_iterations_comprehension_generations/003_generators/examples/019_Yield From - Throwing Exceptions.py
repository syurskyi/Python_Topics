# Yield From - Throwing Exceptions
#
# We have seen that yield from allows us to establish a 2-way communication channel with a subgenerator and we could use
# next, and send to send a "request" to a delegated subgenerator via the delegator generator.
# In fact, we can also send exceptions by throwing an exception into the delegator, just like a send

class CloseCoroutine(Exception):
    pass

def echo():
    try:
        while True:
            received = yield
            print(received)
    except CloseCoroutine:
        return 'coro was closed'
    except GeneratorExit:
        print('closed method was called')

e = echo()
next(e)

e.throw(CloseCoroutine, 'just closing')

e = echo()
next(e)
e.close()

# Yield From - Throwing Exceptions
# As we can see the difference between throw and close is that although close causes an exception to be raised in
# the generator, Python essentially silences it.
# It works the same way when we delegate to the coroutine in a delegator:

def delegator():
    result = yield from echo()
    yield 'subgen closed and returned:', result
    print('delegator closing...')

d = delegator()
next(d)
d.send('hello')

d.throw(CloseCoroutine)

# Yield From - Throwing Exceptions
# Now what happens if the throw in the subgenerator does not close subgenerator but instead silences the exception
# and yields a value instead?

class CloseCoroutine(Exception):
    pass

class IgnoreMe(Exception):
    pass

def echo():
    try:
        while True:
            try:
                received = yield
                print(received)
            except IgnoreMe:
                yield "I'm ignoring you..."
    except CloseCoroutine:
        return 'coro was closed'
    except GeneratorExit:
        print('closed method was called')

d = delegator()
next(d)

d.send('python')

result = d.throw(IgnoreMe, 1000)

result

d.send('rocks!')
d.close()


# Yield From - Throwing Exceptions
# Why did we not get a yielded value back?
# That's because the subgenerator was paused at the yield that yielded "I'm, ignoring you".

# If we want to coroutine to continue running normally after ignoring that exception we need to tweak it slightly:

def echo():
    try:
        output = None
        while True:
            try:
                received = yield output
                print(received)
            except IgnoreMe:
                output = "I'm ignoring you..."
            else:
                output = None
    except CloseCoroutine:
        return 'coro was closed'
    except GeneratorExit:
        print('closed method was called')

d = delegator()
next(d)

d.send('hello')
d.throw(IgnoreMe)
d.send('python')
d.close()

# Yield From - Throwing Exceptions
# What happens if we do not handle the error in the subgenerator and simply let the exception propagate up?
# Who gets the exception, the delegator, or the caller?

def echo():
    while True:
        received = yield
        print(received)

def delegator():
    yield from echo()

d = delegator()
next(d)

d.throw(ValueError)

# Yield From - Throwing Exceptions
# OK, so we, the caller see the exception. But did the delegator see it too? i.e.
# can we catch the exception in the delegator?
# As you can see, we were able to catch the exception in the delegator. Of course, the way we wrote our code,
# the delegator still closed, and hence we now see a StopIteration exception.

def delegator():
    try:
        yield from echo()
    except ValueError:
        print('got the value error')
d = delegator()
next(d)

d.throw(ValueError)

