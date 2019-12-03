# Introduction
#
# Every programmer is acquainted with functions - sequences of instructions grouped together as a single unit in order
# to perform predetermined tasks. They admit a single entry point, are capable of accepting arguments, may or may not
# have a return value, and can be called at any moment during a program's execution - including by other functions and
# themselves.
# When a program calls a function its current execution context is saved before passing control over to the function
# and resuming execution. The function then creates a new context - from there on out newly created data exists
# exclusively during the functions runtime.
# As soon as the task is complete, control is transferred back to the caller - the new context is effectively deleted
# and replaced by the previous one.
# Coroutines
# Coroutines are a special type of function that deliberately yield control over to the caller, but does not end its
# context in the process, instead maintaining it in an idle state.
# They benefit from the ability to keep their data throughout their lifetime and, unlike functions, can have several
# entry points for suspending and resuming execution.
# Coroutines in Python work in a very similar way to Generators. Both operate over data, so let's keep the main
# differences simple:
#     Generators produce data
#     Coroutines consume data
# The distinct handling of the keyword yield determines whether we are manipulating one or the other.

# Defining a Coroutine
# With all the essentials out of the way, let us jump right in and code our first coroutine:

def bare_bones():
    while True:
        value = (yield)

# It's clear to see the resemblance to a regular Python function. The while True: block guarantees the continuous
# execution of the coroutine for as long as it receives values.
# The value is collected through the yield statement. We'll come back to this in a few moments...
# It's clear to see that this code is practically useless, so we'll round it off with a few print statements:

def bare_bones():
    print("My first Coroutine!")
    while True:
        value = (yield)
        print(value)

# Now, what happens when we try to call it like so:
# coroutine = bare_bones()
# If this were a normal Python function, one would expect it to produce some sort of output by this point.
# But if you run the code in its current state you will notice that not a single print() gets called.
# That is because coroutines require the next() method to be called first:

def bare_bones():
    print("My first Coroutine!")
    while True:
        value = (yield)
        print(value)

coroutine = bare_bones()
next(coroutine)

# This starts the execution of the coroutine until it reaches its first breakpoint - value = (yield). Then, it stops,
# returning the execution over to the main, and idles while awaiting new input:
# My first Coroutine!
# New input can be sent with send():
# coroutine.send("First Value")
# Our variable value will then receive the string First Value, print it, and a new iteration of the while True:
# loop forces the coroutine to once again wait for new values to be delivered. You can do this as many times as you like.
# Finally, once you are done with the coroutine and no longer wish to make use of it you can free those resources by
# calling close(). This raises a GeneratorExit exception that needs to be dealt with:

def bare_bones():
    print("My first Coroutine!")
    try:
        while True:
            value = (yield)
            print(value)
    except GeneratorExit:
        print("Exiting coroutine...")

coroutine = bare_bones()
next(coroutine)
coroutine.send("First Value")
coroutine.send("Second Value")
coroutine.close()

# Output:
# My first Coroutine!
# First Value
# Second Value
# Exiting coroutine...

# Passing Arguments
# Much like functions, coroutines are also capable of receiving arguments:

def filter_line(num):
    while True:
        line = (yield)
        if num in line:
            print(line)

cor = filter_line("33")
next(cor)
cor.send("Jessica, age:24")
cor.send("Marco, age:33")
cor.send("Filipe, age:55")

# Output:
#
# Marco, age:33

# Applying Several Breakpoints
# Multiple yield statements can be sequenced together in the same individual coroutine:

def joint_print():
    while True:
        part_1 = (yield)
        part_2 = (yield)
        print("{} {}".format(part_1, part_2))

cor = joint_print()
next(cor)
cor.send("So Far")
cor.send("So Good")

# Output:
# So Far So Good
# The StopIteration Exception

# After a coroutine is closed, calling send() again will generate a StopIteration exception:

def test():
    while True:
        value = (yield)
        print(value)
try:
    cor = test()
    next(cor)
    cor.close()
    cor.send("So Good")
except StopIteration:
    print("Done with the basics")

# Output:
#
# Done with the basics
#
# Coroutines with Decorators
# This is all well and good! But when working in larger projects initiating every single coroutine manually can be such
# a huge drag!
# Worry not, its just the matter of exploiting the power of Decorators so we no longer need to use the next() method:

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

@coroutine
def bare_bones():
    while True:
        value = (yield)
        print(value)

cor = bare_bones()
cor.send("Using a decorator!")

# Running this piece of code will yield:
# Using a decorator!
# Building Pipelines
# A pipeline is a sequence of processing elements organized so that the output of each element is the input of the next.
# Data gets pushed through the pipe until it is eventually consumed. Every pipeline requires at least one source and
# one sink.
# The remaining stages of the pipe can perform several different operations, from filtering to modifying, routing,
# and reducing data:
# Coroutines are natural candidates for performing these operations, they can pass data between one another with send()
# operations and can also serve as the end-point consumer. Let's look at the following example:

def producer(cor):
    n = 1
    while n < 100:
        cor.send(n)
        n = n * 2

@coroutine
def my_filter(num, cor):
    while True:
        n = (yield)
        if n < num:
            cor.send(n)

@coroutine
def printer():
    while True:
        n = (yield)
        print(n)

prnt = printer()
filt = my_filter(50, prnt)
producer(filt)

# Output:
#
# 1
# 2
# 4
# 8
# 16
# 32

# So, what we have here is the producer() acting as the source, creating some values that are then filtered before being
# printed by the sink, in this case, the printer() coroutine.
# my_filter(50, prnt) acts as the single intermediary step in the pipeline and receives its own coroutine as an argument.
# This chaining perfectly illustrates the strength of coroutines: they are scalable for bigger projects
# (all that is required is to add more stages to the pipeline) and easily maintainable (changes to one don't force
# an entire rewrite of the source code).
# Similarities to Objects
# A sharp-eyed programmer might catch on that coroutines contain a certain conceptual similarity to Python objects.
# From the required prior definition to instance declaration and management. The obvious question arises of why one
# would use coroutines over the tried and true paradigm of object-oriented programming.
# Well, aside the obvious fact that coroutines require but a single function definition, they also benefit from being
# significantly faster. Let's examine the following code:

class obj:
    def __init__(self, value):
        self.i = value
    def send(self, num):
        print(self.i + num)

inst = obj(1)
inst.send(5)

def coroutine(value):
    i = value
    while True:
        num = (yield)
        print(i + num)

cor = coroutine(1)
next(cor)
cor.send(5)

# Here's how these two hold up against each other, when ran through the timeit module, 10,000 times:
# Both perform the same menial task but the second example is quicker. Speed gains advent from the absence of the
# object's self lookups.
# For more system-taxing tasks, this feature makes for a compelling reason to use coroutines instead of the conventional
# handler objects.
# Caution when Using Coroutines
# The send() Method is Not Thread-Safe

import threading
from time import sleep

def print_number(cor):
    while True:
        cor.send(1)

def coroutine():
    i = 1
    while True:
        num = (yield)
        print(i)
        sleep(3)
        i += num

cor = coroutine()
next(cor)

t = threading.Thread(target=print_number, args=(cor,))
t.start()

while True:
    cor.send(5)

# Because send() was not properly synchronized, nor does it have inherent protection against thread related miscalls,
#     the following error was raised: ValueError: generator already executing.
# Mixing coroutines with concurrency should be done with extreme caution.
# It's not Possible to Loop Coroutines

def coroutine_1(value):
    while True:
        next_cor = (yield)
        print(value)
        value = value - 1
        if next_cor != None:
            next_cor.send(value)

def coroutine_2(next_cor):
    while True:
        value = (yield)
        print(value)
        value = value - 2
        if next != None:
            next_cor.send(value)

cor1 = coroutine_1(20)
next(cor1)
cor2 = coroutine_2(cor1)
next(cor2)
cor1.send(cor2)

# The same ValueError shows its face. From these simple examples we can infer that the send() method builds a sort of
#     call-stack that doesn't return until the target reaches its yield statement.
# So, using coroutines is not all sunshine and rainbows, careful thought must be had before application.
# Conclusion
# Coroutines provide a powerful alternative to the usual data processing mechanisms. Units of code can be easily combined,
# modified and rewritten, all the while profiting from variable persistence across its life cycle.
# In the hands of a crafty programmer, coroutines become meaningful new tools by allowing simpler design and
    # implementation, all the while providing significant performance gains.
# Stripping ideas down into straightforward processes saves the programmer's effort and time, all the while
    # avoiding stuffing code with superfluous objects that do nothing more than elementary tasks