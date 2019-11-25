print('#' * 52 + '  ### Additional Uses')

import decimal

print(decimal.getcontext())

print('#' * 52 + '  If we create a decimal object, then it will use those settings.')
print('#' * 52 + '  We can certainly change the properties of that global context:')

decimal.getcontext().prec=14
print(decimal.getcontext())

print('#' * 52 + '  And now the default (global) context has a precision set to 14.')
print('#' * 52 + '  Lets reset it back to 28:')

decimal.getcontext().prec = 28

old_prec = decimal.getcontext().prec
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(3))
decimal.getcontext().prec = old_prec
print(decimal.Decimal(1) / decimal.Decimal(3))

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

print('#' * 52 + '  And as you can see, the precision was set back to its original value once the context was exited.')
print('#' * 52 + '  In fact, the decimal class already has a context manager, and its way better than ours,'
                 '  because we can set not only the precision, but anything else we want:')

with decimal.localcontext() as ctx:
    ctx.prec = 3
    print(decimal.Decimal(1) / decimal.Decimal(3))
print(decimal.Decimal(1) / decimal.Decimal(3))

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

with Timer() as timer:
    sleep(1)
print(timer.elapsed)

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

print('back to console output')

with open('test.txt') as f:
    print(f.readlines())

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