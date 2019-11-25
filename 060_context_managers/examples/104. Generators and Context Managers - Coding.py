print('#' * 52 + '  ### Generators and Context Managers')


def my_gen():
    try:
        print('creating context and yielding object')
        lst = [1, 2, 3, 4, 5]
        yield lst
    finally:
        print('exiting context and cleaning up')


gen = my_gen()  # create generator

lst = next(gen)  # enter context and get "as" object
print(lst)

# next(gen)  # exit context    # StopIteration:

print('#' * 52 + '  As you can see, the exiting context code ran.')
print('#' * 52 + '  But to make this cleaner, we will catch the StopIteration exception:')

gen = my_gen()
lst = next(gen)
print(lst)
try:
    next(gen)
except StopIteration:
    pass

print('#' * 52 + '  Now lets write a context manager that can use the type of generator we wrote'
                 '  so we can use it using a `with` statement instead:')


class GenCtxManager:
    def __init__(self, gen_func):
        self._gen = gen_func()

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False


with GenCtxManager(my_gen) as lst:
    print(lst)

print('#' * 52 + '  Our `GenCtxManager` class is not very flexible -'
                 '  we cannot pass arguments to the generator function for example.')
print('#' * 52 + '  We are also not doing any exception handling...')


class GenCtxManager:
    def __init__(self, gen_func, *args, **kwargs):
        self._gen = gen_func(*args, **kwargs)

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

def open_file(fname, mode):
    try:
        print('opening file...')
        f = open(fname, mode)
        yield f
    finally:
        print('closing file...')
        f.close()

with GenCtxManager(open_file, 'test.txt', 'w') as f:
    print('writing to file...')
    f.write('testing...')

print('#' * 52 + '  ')

with open('test.txt') as f:
    print(next(f))

