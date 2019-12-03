# We all are familiar with function which is also known as a subroutine, procedure, subprocess etc. A function is a
# sequence of instructions packed as a unit to perform a certain task. When the logic of a complex function is divided
# into several self-contained steps that are themselves functions, then these functions are called helper functions or
# subroutines.
# Subroutines in Python are called by main function which is responsible for coordination the use of these subroutines.
# Subroutines have single entry point.

# Coroutines are generalization of subroutines. They are used for cooperative multitasking where a process voluntarily
# yield (give away) control periodically or when idle in order to enable multiple applications to be run simultaneously.
# The difference between coroutine and subroutine is :
# Unlike subroutines, coroutines have many entry points for suspending and resuming execution. Coroutine can suspend
# its execution and transfer control to other coroutine and can resume again execution from the point it left off.
# Unlike subroutines, there is no main function to call coroutines in particular order and coordinate the results.
# Coroutines are cooperative that means they link together to form a pipeline. One coroutine may consume input data
# and send it to other which process it. Finally there may be a coroutine to display result.

# Now you might be thinking how coroutine is different from threads, both seems to do same job.
# In case of threads, it’s operating system (or run time environment) that switches between threads according to
# the scheduler. While in case of coroutine, it’s the programmer and programming language which decides when to switch
# coroutines. Coroutines work cooperatively multi task by suspending and resuming at set points by programmer.
#
# Python Coroutine
#
# In Python, coroutines are similar to generators but with few extra methods and slight change in how we use yield
# statement. Generators produce data for iteration while coroutines can also consume data.
# In Python 2.5, a slight modification to the yield statement was introduced, now yield can also be used as expression.
# For example on the right side of the assignment –
# line = (yield)
#
# whatever value we send to coroutine is captured and returned by (yield) expression.
# A value can be send to the coroutine by send() method. For example, consider this coroutine which print out name
# having prefix “Dear” in it. We will send names to coroutine using send() method.

# Python3 program for demonstrating
# coroutine execution

def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)

# calling coroutine, nothing will happen
corou = print_name("Dear")

# This will start execution of coroutine and
# Prints first line "Searchig prefix..."
# and advance execution to the first yield expression
corou.__next__()

# sending inputs
corou.send("Atul")
corou.send("Dear Atul")

# Output:
#
# Searching prefix:Dear
# Dear Atul

# Execution of coroutine is similar to the generator. When we call coroutine nothing happens, it runs only in response
# to the next() and send() method. This can be seen clearly in above example, as only after calling __next__() method,
# out coroutine starts executing. After this call, execution advances to the first yield expression, now execution
# pauses and wait for value to be sent to corou object. When first value is sent to it, it checks for prefix and print
# name if prefix present. After printing name it goes through loop until it encounters name = (yield) expression again.
#
# Closing a Coroutine
#
# Coroutine might run indefinitely, to close coroutine close() method is used. When coroutine is closed it generates
# GeneratorExit exception which can be catched in usual way. After closing coroutine, if we try to send values,
# it will raise StopIteration exception. Following is a simple example :


# Python3 program for demonstrating
# closing a coroutine

def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")


corou = print_name("Dear")
corou.__next__()
corou.send("Atul")
corou.send("Dear Atul")
corou.close()

# Output:
#
# Searching prefix:Dear
# Dear Atul
# Closing coroutine!!

# Chaining coroutines for creating pipeline
#
# Coroutines can be used to set pipes. We can chain together coroutines and push data through pipe using send() method. A pipe needs :
#
#         An initial source(producer) which derives the whole pipe line. Producer is usually not a coroutine, it’s just a simple method.
#         A sink, which is the end point of the pipe. A sink might collect all data and display it.
#
# pipeline
# Following is a simple example of chaining –


# Python3 program for demonstrating
# coroutine chaining

def producer(sentence, next_coroutine):
    '''
    Producer which just split strings and
    feed it to pattern_filter coroutine
    '''
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
    '''
    Search for pattern in received token
    and if pattern got matched, send it to
    print_token() coroutine for printing
    '''
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with filtering!!")


def print_token():
    '''
    Act as a sink, simply print the
    received tokens
    '''
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine=pt)
pf.__next__()

sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)

# Output:
#
# I'm sink, i'll print tokens
# Searching for ing
# running
# moving
# Done with filtering!!
# Done with printing!


