# Nested Context Managers
# In the last video we saw that we could nest context managers.
# This is actually fairly common.
# Suppose we need to open a number of files - using a with statement for each one means we would have to nest that
# many with statements as well.
# For example, we want to "zip" three files. Let's look at the content of each file first:

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
# file1_line1
# file1_line2
# file1_line3
# ----------------
# file2_line1
# file2_line2
# file2_line3
# ----------------
# file3_line1
# file3_line2
# file3_line3
# ######################################################################################################################

# Now we want to combine the rows from each file, and print them out - like zipping together basically, except
# we need to strip out that pesky \n!
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
# file1_line1,file2_line1,file3_line1
# file1_line2,file2_line2,file3_line2
# file1_line3,file2_line3,file3_line3
# ######################################################################################################################


# As you can see we needed three levels of nested with statements.
# Instead, we might try to approach the problem this way - but first let's write our own openfile context manager
# so we can easily see when the file is being opened and closed
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

# First we are going to create (but not enter) the context managers, and store the enter and exit methods in some lists.
# We'll also create a list that will contain the values returned by the enter methods:


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

# Now, we are going to enter the contexts by calling the __enter__ methods, store the return values (the file objects),
# process the data, and then run all the __exit__ methods (in reverse order!):

files = [enter() for enter in enters]
# opening file file1.txt
# opening file file2.txt
# opening file file3.txt
# ######################################################################################################################

print('#' * 52 + '  ')

while True:
    try:
        rows = [next(f).strip('\n') for f in files]
    except StopIteration:
        break
    else:
        row = ','.join(rows)
        print(row)
# file1_line1,file2_line1,file3_line1
# file1_line2,file2_line2,file3_line2
# file1_line3,file2_line3,file3_line3
# ######################################################################################################################

# Now, we need to close all the files by calling the __exit__ methods (in reverse order, since we aded them in
# the order in which the contexts were opened (i.e. we open from first file to last, but close from last opened file
# to first - think of how the context managers are nested).
# Also, keep in mind that __exit__ methods need those exception parameters - here we'll just use None for simplicity -
# we are not doing any exception handling!

print('#' * 52 + '  ')

for fn in exits[::-1]:
    fn(None, None, None)
# closing file file3.txt
# closing file file2.txt
# closing file file1.txt
# ######################################################################################################################

# So, let's recap by putting all this code together and simplifying a few things along the way:

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
# opening file file1.txt
# opening file file2.txt
# opening file file3.txt
# file1_line1,file2_line1,file3_line1
# file1_line2,file2_line2,file3_line2
# file1_line3,file2_line3,file3_line3
# closing file file3.txt
# closing file file2.txt
# closing file file1.txt
# ######################################################################################################################

# What was simpler, this method or simply nesting the with blocks?
# What if we were doing this with 100 files instead of just 3?
# Or what if we did not know in advance how many files we had to zip together (maybe we're reading all the .txt
# files in a directory for example - there may be 1 file, 3 files, 10 files, we don't realy know,
# and it can change over time)?
# Maybe we can find a way to make this a little easier to use.
# Let's try using a context manager to hold on to all these __exit__ methods we want to use:

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

# opening file file1.txt
# opening file file2.txt
# opening file file3.txt
# do work here
# closing file file3.txt
# closing file file2.txt
# closing file file1.txt
# ######################################################################################################################

# As you can see, the files were opened, our work was done, and the files were closed. Let's just add in some real work:

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
# opening file file1.txt
# opening file file2.txt
# opening file file3.txt
# file1_line1,file2_line1,file3_line1
# file1_line2,file2_line2,file3_line2
# file1_line3,file2_line3,file3_line3
# closing file file3.txt
# closing file file2.txt
# closing file file1.txt
# ######################################################################################################################

# This is much better, but specifying the context managers is still a little painful, having to list them all
# separately as the arguments to the NestedContexts manager.
#
# We could simplify things somewhat by taking this approach:

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
# opening file file1.txt
# opening file file2.txt
# opening file file3.txt
# file1_line1,file2_line1,file3_line1
# file1_line2,file2_line2,file3_line2
# file1_line3,file2_line3,file3_line3
# closing file file3.txt
# closing file file2.txt
# closing file file1.txt
# ######################################################################################################################

# So, this works, and is actually quite workable, but we have to do some setup work before we can use
# the context manager.
# We can try a slightly different approach where we create a method in our NestedContextManager that can be used
# to "register" contexts - so instead of creating the NestedContextManager with an __init__ that takes in all
# the contexts at once, we create the NextedContextManager first, and then, inside the with block we append
# the contexts we want to work with.
# One main advantage to that approach is that we can add contexts to NestedContextManager at any time in
# the with block - i.e. we can delay when and how we add contexts to the overarching context manager.
# So, we'll do this by implementing a method in NestedContexts itself that will allow us to append a context manager,
# get the __enter__ value out of it, and store the __exit__ methods.
# To do this we're going to take a slightly different approach - the NestedContexts manager is going to return
# itself in it's __enter__ method, instead of returning a list of the various context values returned
# from their respective __enter__ methods:

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')


class NestedContexts:
    def __init__(self):
        self._exits = []

    def __enter__(self):
        return self

    def enter_context(self, ctx):
        self._exits.append(ctx.__exit__)
        value = ctx.__enter__()
        return value

    def __exit__(self, exc_type, exc_value, exc_tb):
        for exit in self._exits[::-1]:
            exit(exc_type, exc_value, exc_tb)
        return False

# Now let's try it again, but this time we'll "register" our contexts once the NestedContexts context has been entered:


f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with NestedContexts() as stack:
    files = [stack.enter_context(open_file(f_name)) for f_name in f_names]
# opening file file1.txt
# opening file file2.txt
# opening file file3.txt
# closing file file3.txt
# closing file file2.txt
# closing file file1.txt

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
# opening file file1.txt
# opening file file2.txt
# opening file file3.txt
# file1_line1,file2_line1,file3_line1
# file1_line2,file2_line2,file3_line2
# file1_line3,file2_line3,file3_line3
# closing file file3.txt
# closing file file2.txt
# closing file file1.txt
# ######################################################################################################################

# Hopefully you can now see why I said we can decide to add contyexts to that stack at any time inside
# the with statement - we are not restricted to adding them in the __init__ - which means we can even use
# if statements to add contexts to the stack if we want to - this is far more flexible.
# So, this is a common enough scenario that the standard library has something up its sleeve for us!
# The contextlib has an ExitStack context manager that works the same way as our NestedContexts, but,
# unlike our approach, it actually does exception handling properly too!
# Let's see how we use it:

print('#' * 52 + '  The `contextlib` has an `ExitStack` context manager that works the same way as'
                 '  our `NestedContexts`, but, unlike our approach, it actually does exception handling properly too!')

from contextlib import ExitStack

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with ExitStack() as stack:
    files = [stack.enter_context(open_file(f_name)) for f_name in f_names]
# opening file file1.txt
# opening file file2.txt
# opening file file3.txt
# closing file file3.txt
# closing file file2.txt
# closing file file1.txt
# ######################################################################################################################

# As you can see, the files were opened and automatically closed. Now all we need to do is the work itself:

print('#' * 52 + '  As you can see, the files were opened and automatically closed.'
                 '  Now all we need to do is the work itself:')

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with ExitStack() as stack:
    files = [stack.enter_context(open_file(f_name)) for f_name in f_names]
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)
# opening file file1.txt
# opening file file2.txt
# opening file file3.txt
# file1_line1,file2_line1,file3_line1
# file1_line2,file2_line2,file3_line2
# file1_line3,file2_line3,file3_line3
# closing file file3.txt
# closing file file2.txt
# closing file file1.txt
# ######################################################################################################################


# To finish up we can use the built-in open context manager:
print('#' * 52 + '  To finish up we can use the built-in `open` context manager:')


f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with ExitStack() as stack:
    files = [stack.enter_context(open(f_name)) for f_name in f_names]
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)
# file1_line1,file2_line1,file3_line1
# file1_line2,file2_line2,file3_line2
# file1_line3,file2_line3,file3_line3
