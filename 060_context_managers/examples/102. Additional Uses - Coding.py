print('#' * 52 + '  ### Additional Uses')
# Additional Uses
# Remember what I said in the last lecture about some common patterns we can implement with context managers:
#     Open - Close
#     Change - Reset
#     Start - Stop
# The open file context manager is an example of the Open - Close pattern. But we have other ones as well.
# Decimal Contexts
# Decimals have a context which can be used to define many things, such as precision, rounding mechanism, etc.
# By default, Decimals have a "global" context - i.e. one that will apply to any Decimal object by default:

import decimal

print(decimal.getcontext())
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[],
# traps=[InvalidOperation, DivisionByZero, Overflow])
# ######################################################################################################################

# If we create a decimal object, then it will use those settings.
# We can certainly change the properties of that global context:
print('#' * 52 + '  If we create a decimal object, then it will use those settings.')
print('#' * 52 + '  We can certainly change the properties of that global context:')

decimal.getcontext().prec=14
print(decimal.getcontext())
# Context(prec=14, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[],
# traps=[InvalidOperation, DivisionByZero, Overflow])
# ######################################################################################################################

# And now the default (global) context has a precision set to 14.
# Let's reset it back to 28:
print('#' * 52 + '  And now the default (global) context has a precision set to 14.')
print('#' * 52 + '  Lets reset it back to 28:')

decimal.getcontext().prec = 28

# Suppose now that we just want to temporarily change something in the context - we would have to do something like
# this:

old_prec = decimal.getcontext().prec
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(3))
decimal.getcontext().prec = old_prec
print(decimal.Decimal(1) / decimal.Decimal(3))
# 0.3333
# 0.3333333333333333333333333333
# ######################################################################################################################

# Of course, this is kind of a pain to have to store the current value, set it to something new, and then remember
# to set it back to it's original value.
# How about writing a context manager to do that seamlessly for us:
print('#' * 52 + '  Of course, this is kind of a pain to have to store the current value, set it to something new,'
                 '  and then remember to set it back to its original value.')
print('#' * 52 + '  How about writing a context manager to do that seamlessly for us:')


class precision:
    def __init__(self, prec):
        self.prec = prec
        self.current_prec = decimal.getcontext().prec

    def __enter__(self):
        decimal.getcontext().prec = self.prec

    def __exit__(self, exc_type, exc_value, exc_traceback):
        decimal.getcontext().prec = self.current_prec
        return False


with precision(3):
    print(decimal.Decimal(1) / decimal.Decimal(3))
print(decimal.Decimal(1) / decimal.Decimal(3))
# 0.333
# 0.3333333333333333333333333333
# ######################################################################################################################

# And as you can see, the precision was set back to it's original value once the context was exited.
# In fact, the decimal class already has a context manager, and it's way better than ours, because we can set not only
# the precision, but anything else we want:
print('#' * 52 + '  And as you can see, the precision was set back to its original value once the context was exited.')
print('#' * 52 + '  In fact, the decimal class already has a context manager, and its way better than ours,'
                 '  because we can set not only the precision, but anything else we want:')

with decimal.localcontext() as ctx:
    ctx.prec = 3
    print(decimal.Decimal(1) / decimal.Decimal(3))
print(decimal.Decimal(1) / decimal.Decimal(3))
# 0.333
# 0.3333333333333333333333333333
# ######################################################################################################################

# Timing a with block
#
# Here's another example of a Start - Stop type of context manager. We'll create a context manager to time the code
# inside the with block:
print('#' * 52 + '  #### Timing a with block')
print('#' * 52 + '  Here is another example of a **Start - Stop** type of context manager.')
print('#' * 52 + '  We will create a context manager to time the code inside the `with` block:')

from time import perf_counter, sleep


class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False

# You'll note that this time we are returning the context manager itself from the __enter__ statement.
# This will allow us to look at the elapsed property of the context manager once the with statement
# has finished running.


with Timer() as timer:
    sleep(1)
print(timer.elapsed)
# 0.9993739623039163
# ######################################################################################################################

# Redirecting stdout
# Here we are going to temporarily redirect stdout to a file instead fo the console:
print('#' * 52 + '  #### Redirecting stdout')
print('#' * 52 + '  Here we are going to temporarily redirect `stdout` to a file instead fo the console:')

import sys


class OutToFile:
    def __init__(self, fname):
        self._fname = fname
        self._current_stdout = sys.stdout

    def __enter__(self):
        self._file = open(self._fname, 'w')
        sys.stdout = self._file

    def __exit__(self, exc_type, exc_value, exc_tb):
        sys.stdout = self._current_stdout
        if self._file:
            self._file.close()
        return False


with OutToFile('test.txt'):
    print('Line 1')
    print('Line 2')

# As you can see, no output happened on the console... Instead the output went to the file we specified.
# And our print statements will now output to the console again:

print('back to console output')

# back to console output

with open('test.txt') as f:
    print(f.readlines())


# HTML Tags
# In this example, we're going to basically use a context manager to inject opening and closing html tags as
# we print to the console (of course we could redirect our prints somewhere else as we just saw!):
print('#' * 52 + '  #### HTML Tags')


class Tag:
    def __init__(self, tag):
        self._tag = tag

    def __enter__(self):
        print(f'<{self._tag}>', end='')

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f'</{self._tag}>', end='')
        return False

with Tag('p'):
    print('some ', end='')
    with Tag('b'):
        print('bold', end='')
    print(' text', end='')

# <p>some <b>bold</b> text</p>
# ######################################################################################################################

# Re-entrant Context Managers
# We can also write context managers that can be re-entered in the sense that we can call __enter__ and __exit__
# more than once on the same context manager.
# These methods are called when a with statement is used, so we'll need to be able to get our hands on the context
# manager object itself - but that's easy, we just return self from the __enter__ method.
# Let's write a ListMaker context manager to do see how this works.
print('#' * 52 + '  #### Re-entrant Context Managers')
print('#' * 52 + '  Let is write a ListMaker context manager to do see how this works.')


class ListMaker:
    def __init__(self, title, prefix='- ', indent=3):
        self._title = title
        self._prefix = prefix
        self._indent = indent
        self._current_indent = 0
        print(title)

    def __enter__(self):
        self._current_indent += self._indent
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._current_indent -= self._indent
        return False

    def print(self, arg):
        s = ' ' * self._current_indent + self._prefix + str(arg)
        print(s)

# Because __enter__ is returning self, the instance of the context manager, we can call with on that context manager
# and it will automatically call the __enter__ and __exit__ methods. Each time we run __enter__ we increase
# the indentation, each time we run __exit__ we decrease the indentation.
# Our print method then takes that into account when it prints the requested string argument.


print('#' * 52 + '  Our `print` method then takes that into account when it prints the requested string argument.')

with ListMaker('Items') as lm:
    lm.print('Item 1')
    with lm:
        lm.print('item 1a')
        lm.print('item 1b')
    lm.print('Item 2')
    with lm:
        lm.print('item 2a')
        lm.print('item 2b')
# Items
#    - Item 1
#       - item 1a
#       - item 1b
#    - Item 2
#       - item 2a
#       - item 2b
# ######################################################################################################################

# Of course, we can easily redirect the output to a file instead, using the context manager we wrote earlier:
print('#' * 52 + '  Of course, we can easily redirect the output to a file instead,'
                 '  using the context manager we wrote earlier:')

with OutToFile('my_list.txt'):
    with ListMaker('Items') as lm:
        lm.print('Item 1')
        with lm:
            lm.print('item 1a')
            lm.print('item 1b')
        lm.print('Item 2')
        with lm:
            lm.print('item 2a')
            lm.print('item 2b')

with open('my_list.txt') as f:
    for row in f:
        print(row, end='')
# Items
#    - Item 1
#       - item 1a
#       - item 1b
#    - Item 2
#       - item 2a
#       - item 2b
# ######################################################################################################################
