print('#' * 52 + '  ### Using Decorators to Create Context Managers using Generator Functions')

def open_file(fname, mode='r'):
    print('opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file...')
        f.close()


class GenContextManager:
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        return next(self.gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('calling next to perform cleanup in generator')
        try:
            next(self.gen)
        except StopIteration:
            pass
        return False

file_gen = open_file('test.txt', 'w')

with GenContextManager(file_gen) as f:
    f.writelines('Sir Spamalot')

print('#' * 52 + '  And we can read back from the file too:')

file_gen = open_file('test.txt')
with GenContextManager(file_gen) as f:
    print(f.readlines())

print('#' * 52 + '  We still have to create the generator object from the generator function before'
                 '  we can use the context manager class.')
print('#' * 52 + '  We can simplify things even more by using a decorator:')

def context_manager_dec(gen_fn):
    def helper(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        ctx = GenContextManager(gen)
        return ctx
    return helper

@context_manager_dec
def open_file(fname, mode='r'):
    print('opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file...')
        f.close()

with open_file('test.txt') as f:
    print(f.readlines())

print('#' * 52 + '  So now we have an approach to using a decorator to turn any generator function'
                 '  (that has the structure we mentioned earlier) into a context manager!')

from contextlib import contextmanager

@contextmanager
def open_file(fname, mode='r'):
    print('opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file...')
        f.close()

with open_file('test.txt') as f:
    print(f.readlines())

print('#' * 52 + '  Lets implement a timer.')

from time import perf_counter, sleep

@contextmanager
def timer():
    stats = dict()
    start = perf_counter()
    stats['start'] = start
    try:
        yield stats
    finally:
        end = perf_counter()
        stats['end'] = end
        stats['elapsed'] = end - start

with timer() as stats:
    sleep(1)

print(stats)

print('#' * 52 + '  In this example, lets redirect `stdout`.')

import sys

@contextmanager
def out_to_file(fname):
    current_stdout = sys.stdout
    file = open(fname, 'w')
    sys.stdout = file
    try:
        yield None
    finally:
        file.close()
        sys.stdout = current_stdout

with out_to_file('test.txt'):
    print('line 1')
    print('line 2')

with open('test.txt') as f:
    print(f.readlines())

print('#' * 52 + '  And of course, `stdout` is back to "normal":')

print('line 1')

print('#' * 52 + '  The `contextlib` module actually implements a `stdout` redirect context manager,'
                 '  so we technically dont have to write one ourselves.')

from contextlib import redirect_stdout

with open('test.txt', 'w') as f:
    with redirect_stdout(f):
        print('Look on the bright side of life')

with open('test.txt') as f:
    print(f.readlines())