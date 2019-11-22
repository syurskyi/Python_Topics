# Sending data to Generators

# With PEP 342, generators were enhanced to allow not just sending data out (yielding), but also receiving data.
# The basic idea is that when a generator is suspended after a yield statement,
# why not allow sending it some data when we resume its execution, exactly at the point where it resumes.
# In other words, immediately after the yield statement.
# And not on the next line of code, but actually in the same line as the yield -
# we should now think of the yield keyword, not just as a statement, but as an expression that also receives data -
# and we can assign that received value to a variable using an assignment. We can send data to the suspended generator
# (and resume running it) by using the send() method of the generator (instead of just using the __next__ method
# (or, same thing, next()).
# Note: The same yield keyword is actually used to do both - but make no mistake,
# these are very different usages of the same keyword.
#
# The key difference is that yield is actually an expression, not a simple statement -
# and of course we can assign expressions to variables.

# Sending data to Generators
# simple example
# We now have a generator object, but what is it's state?
# t will first evaluate the right hand side - at which time it will yield and therefore become suspended!
# Now that it is waiting to resume, we can send it data, and the generator will received that data as if it were
# the right hand side of the assignment:
# And now the generator continued running until it hit a yield again -
# which it does since we have our yield inside an infinite loop:
# So, the send method essentially resume the generator just as the __next__ does - but it also sends in some data
# that we can capture if we want to, inside the generator.
# What happens if we do call next() or __next__ instead of send()?
# The same as if we had sent the None value:

def echo():
    while True:
        received = yield
        print('You said:', received)

e = echo()

from inspect import getgeneratorstate
getgeneratorstate(e)
next(e)
getgeneratorstate(e)
e.send('python')
e.send('I said')
next(e)
next(None)

# Sending data to Generators
#
# At this point we can see that generators can be used to both send and receive data.

def squares(n):
    for i in range(n):
        received = yield i ** 2
        print('received:', received)

sq = squares(5)
next(sq)

yielded = sq.send('hello')
print('yielded:', yielded)

yielded = sq.send('hello')
print('yielded:', yielded)

# Sending data to Generators
# Of course, once the generator no longer yields, but returns we'll get the same StopIteration exception:
# The next send is going to resume the generator, it will print what we send it, and continue running -
# but this time the loop is done, so it will print our final that's all, folks, and the function will return (None)
# and hence cause a StopIteration exception to be raised:

def echo(max_times):
    for i in range(max_times):
        received = yield
        print('You said:', received)
    print("that's all, folks!")

e = echo(3)
next(e)

e.send('python')
e.send('is')

e.send('awesome')

# Sending data to Generators
#
# Consider this example where we want a generator/coroutine that maintains (and yields) a running average of values
# we send it.
# Let's first see how we would do it without using a coroutine - instead we'll use a closure so we can maintain
# the state (total and count):
# And now the same, but using a coroutine:

def averager():
    total = 0
    count = 0
    def inner(value):
        nonlocal total
        nonlocal count
        total += value
        count += 1
        return total / count
    return inner

def running_averages(iterable):
    avg = averager()
    for value in iterable:
        running_average = avg(value)
        print(running_average)

running_averages([1, 2, 3, 4])

def running_averager():
    total = 0
    count = 0
    running_average = None
    while True:
        value = yield running_average
        total += value
        count += 1
        running_average = total / count

def running_averages(iterable):
    averager = running_averager()
    next(averager)  # prime generator
    for value in iterable:
        running_average = averager.send(value)
        print(running_average)

running_averages([1, 2, 3, 4])
