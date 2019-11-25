print('#' * 52 + '  ### Nested Context Managers')

with open('file1.txt') as f:
    for row in f:
        print(row, end='')
print('\n----------------')
with open('file2.txt') as f:
    for row in f:
        print(row, end='')
print('\n----------------')
with open('file3.txt') as f:
    for row in f:
        print(row, end='')

print(
    '#' * 52 + '  Now we want to combine the rows from each file, and print them out - like zipping together basically,'
               '  except we need to strip out that pesky `n`!')

with open('file1.txt') as f1:
    with open('file2.txt') as f2:
        with open('file3.txt') as f3:
            while True:
                try:
                    f1_row = next(f1).strip('\n')
                    f2_row = next(f2).strip('\n')
                    f3_row = next(f3).strip('\n')
                except StopIteration:
                    break
                else:
                    print(f1_row + ',' + f2_row + ',' + f3_row)

print('#' * 52 + '  As you can see we needed three levels of nested `with` statements.')

from contextlib import contextmanager


@contextmanager
def open_file(f_name):
    print(f'opening file {f_name}')
    f = open(f_name)
    try:
        yield f
    finally:
        print(f'closing file {f_name}')
        f.close()


print('#' * 52 + '  First we are going to create (but not enter) the context managers,'
                 '  and store the enter and exit methods in some lists.')
print('#' * 52 + '  We will also create a list that will contain the values returned by the enter methods:')

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

enters = []
exits = []
for f_name in f_names:
    ctx = open_file(f_name)
    enters.append(ctx.__enter__)
    exits.append(ctx.__exit__)

files = [enter() for enter in enters]

print('#' * 52 + '  ')

while True:
    try:
        rows = [next(f).strip('\n') for f in files]
    except StopIteration:
        break
    else:
        row = ','.join(rows)
        print(row)

print('#' * 52 + '  ')

for fn in exits[::-1]:
    fn(None, None, None)

print('#' * 52 + '  So, lets recap by putting all this code together and simplifying a few things along the way:')

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

exits = []
files = []
try:
    for f_name in f_names:
        ctx = open_file(f_name)
        files.append(ctx.__enter__())
        exits.append(ctx.__exit__)

    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)
finally:
    for fn in exits[::-1]:
        fn(None, None, None)

print('#' * 52 + '  Lets try using a context manager to hold on to all these `__exit__` methods we want to use:')


class NestedContexts:
    def __init__(self, *contexts):
        self._enters = []
        self._exits = []
        self._values = []

        for ctx in contexts:
            self._enters.append(ctx.__enter__)
            self._exits.append(ctx.__exit__)

    def __enter__(self):
        for enter in self._enters:
            self._values.append(enter())
        return self._values

    def __exit__(self, exc_type, exc_value, exc_tb):
        for exit in self._exits[::-1]:
            exit(exc_type, exc_value, exc_tb)
        return False

with NestedContexts(open_file('file1.txt'),
                   open_file('file2.txt'),
                   open_file('file3.txt')) as files:
    print('do work here')

print('#' * 52 + '  As you can see, the files were opened, our work was done, and the files were closed.')

with NestedContexts(open_file('file1.txt'),
                   open_file('file2.txt'),
                   open_file('file3.txt')) as files:
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)

print('#' * 52 + '  This is much better, but specifying the context managers is still a little painful,'
                 '  having to list them all separately as the arguments to the `NestedContexts` manager.')
print('#' * 52 + '  We could simplify things somewhat by taking this approach:')

file_names = 'file1.txt', 'file2.txt', 'file3.txt'
contexts = [open_file(f_name) for f_name in f_names]
with NestedContexts(*contexts) as files:
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with NestedContexts() as stack:
    files = [stack.enter_context(open_file(f_name)) for f_name in f_names]

print('#' * 52 + '  Nice! Now lets just do the work as well:')

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with NestedContexts() as stack:
    files = [stack.enter_context(open_file(f_name)) for f_name in f_names]

    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)

print('#' * 52 + '  The `contextlib` has an `ExitStack` context manager that works the same way as'
                 '  our `NestedContexts`, but, unlike our approach, it actually does exception handling properly too!')

from contextlib import ExitStack

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with ExitStack() as stack:
    files = [stack.enter_context(open_file(f_name))
            for f_name in f_names]

print('#' * 52 + '  As you can see, the files were opened and automatically closed.'
                 '  Now all we need to do is the work itself:')

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with ExitStack() as stack:
    files = [stack.enter_context(open_file(f_name))
            for f_name in f_names]
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)

print('#' * 52 + '  To finish up we can use the built-in `open` context manager:')


f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with ExitStack() as stack:
    files = [stack.enter_context(open(f_name))
            for f_name in f_names]
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)



