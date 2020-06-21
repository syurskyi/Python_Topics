import time
from contextlib import contextmanager

@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))

# Example use
with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1

# Problem
# You want to implement new kinds of context managers for use with the with statement.
# Solution
# One of the most straightforward ways to write a new context manager is to use the
# @contextmanager decorator in the contextlib module. Here is an example of a context
# manager that times the execution of a code block:

# In the timethis() function, all of the code prior to the yield executes as the __en
# ter__() method of a context manager. All of the code after the yield executes as the
# __exit__() method. If there was an exception, it is raised at the yield statement.
# Here is a slightly more advanced context manager that implements a kind of transaction
# on a list object:

# The idea here is that changes made to a list only take effect if an entire code block runs
# to completion with no exceptions. Here is an example that illustrates:

# Discussion
# Normally, to write a context manager, you define a class with an __enter__() and
# __exit__() method, like this:

# Although this isn’t hard, it’s a lot more tedious than writing a simple function using
# @contextmanager.
# @contextmanager is really only used for writing self-contained context-management
# functions. If you have some object (e.g., a file, network connection, or lock) that needs
# to support the with statement, you still need to implement the __enter__() and
# __exit__() methods separately.