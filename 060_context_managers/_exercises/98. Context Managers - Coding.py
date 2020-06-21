# # You should be familiar with try and finally.
# #
# # We use the finally block to make sure a piece of code is executed, whether an exception has happened or not:
#
# print('#' * 52 + '  You should be familiar with `try` and `finally`.')

try:
    10 / 2
except ZeroDivisionError:
    print('Zero division exception occurred')
finally:
    print('finally ran!')

print('#' * 52 + '  ')

# finally ran!

try:
    1 / 0
except ZeroDivisionError:
    print('Zero division exception occurred')
finally:
    print('finally ran!')

print('#' * 52 + '  You will see that in both instances, the `finally` block was executed.'
                 '  Even if an exception is raised in the `except` block, the `finally` block will **still** execute!')

print(
    '#' * 52 + 'Even if the finally is in a function and there is a return statement in the `try` or `except` blocks:')

# Zero division exception occurred
# finally ran!
# ######################################################################################################################
# You'll see that in both instances, the finally block was executed. Even if an exception is raised in the except block,
# the finally block will still execute!
# Even if the finally is in a function and there is a return statement in the try or except blocks:


def my_func():
    try:
        1 / 0
    except:
        return
    finally:
        print('finally running...')


my_func()

print('#' * 52 + '  This is very handy to release resources even in cases where an exception occurs. ')
print('#' * 52 + '  For example making sure a file is closed after being opened:')

try:
    f = open('test.txt', 'w')
    a = 1 / 0
except:
    print('an exception occurred...')
finally:
    print('Closing file...')
    f.close()

# We should always do that when dealing with files.
# But that can get cumbersome...
# So, there is a better way.
# Let's talk about context managers, and the pattern we are trying to solve:
#     Run some code to create some object(s)
#     Work with object(s)
#     Run some code when done to clean up object(s)
# Context managers do precisely that.
# We use a context manager to create and clean up some objects. The key point is that the cleanup needs to happens
# automatically - we should not have to write code such as the try...except...finally code we saw above.
# When we use context managers in conjunction with the with statement, we end up with the "cleanup" phase happening as
# soon as the with statement finishes:


print('#' * 52 + '  We should **always** do that when dealing with files.')
print('#' * 52 + '  ')
print('#' * 52 + '  When we use context managers in conjunction with the `with` statement,'
                 '  we end up with the "cleanup" phase happening as soon as the `with` statement finishes:')

with open('test.txt', 'w') as file:
    print('inside with: file closed?', file.closed)
print('after with: file closed?', file.closed)
# inside with: file closed? False
# after with: file closed? True
# ######################################################################################################################

print('#' * 52 + '  This works even in this case:')


def test():
    with open('test.txt', 'w') as file:
        print('inside with: file closed?', file.closed)
        return file

# As you can see, we return directly out of the with block...


file = test()
# inside with: file closed? False

print(file.closed)
# True

print('#' * 52 + '  And yet, the file was still closed.')
print('#' * 52 + '  It also works even if we have an exception in the middle of the block')
# with open('test.txt', 'w') as f:
#     print('inside with: file closed?', f.closed)
#     raise ValueError()                              ###### ValueError:
# ######################################################################################################################

print('after with: file closed?', f.closed)
# after with: file closed? True

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')

# Context managers can be used for more than just opening and closing files.
# If we think about it there are two phases to a context manager:
#     when the with statement is executing: we enter the context
#     when the with block is done: we exit the context
# We can create our own context manager using a class that implements an __enter__ method which is executed when
# we enter the context, and an __exit__ method that is executed when we exit the context.
# There is a general pattern that context managers can help us deal with:
#     Open - Close
#     Lock - Release
#     Change - Reset
#     Enter - Exit
#     Start - Stop
# The __enter__ method is quite straightforward. It can (but does not have to) return one or more objects we then
# use inside the with block.
# The __exit__ method however is slightly more complicated.
#     It needs to return a boolean True/False. This indicates to Python whether to suppress any errors that occurred
#     in the with block. As we saw with files, that was not the case - i.e. it returns a False
#     If an error does occur in the with block, the error information is passed to the __exit__ method - so it needs
#     three things: the exception type, the exception value and the traceback. If no error occured, then those values
#     will simply be None.
#
# We haven't covered exceptions in detail yet, so let's quickly see what those three things are:


# ___ my_func
#     return 1.0 / 0.0
# my_func()  # Z.....: float division by zero
# ######################################################################################################################

print('#' * 52 + '  Lets go ahead and create a context manager:')

# The exception type here is Z......
# The exception value is float division by zero.
# The traceback is an object of type traceback (that itself points to other traceback objects forming the trace stack)
# used to generate that text shown in the output.
# I am not going to cover traceback objects at this point - we'll do this in a future part (OOP) of this series.
# Let's go ahead and create a context manager:


class MyContext:
    def __init__(self):
        self.obj = None

    def __entet__(self):
        print('entering context...')
        self.obj = 'the Return Object'
        retrun self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting context...')
        if exc_type:
            print(f'*** Error occurred: {exc_type}, {exc_val}')
        return False  # do not suppress exceptions

# with MyContext() as obj:
#     raise ValueError    # ValueError:


# As you can see, the __exit__ method was still called - which is exactly what we wanted in the first place. Also,
# the exception that was raise inside the with block is seen.
# We can change that by returning True from the __exit__ method:


# print('#' * 52 + '  As you can see, the `__exit__` method was still called -'
#                  '  which is exactly what we wanted in the first place.')
# print('#' * 52 + '   Also, the exception that was raise inside the `with` block is seen.')
# print('#' * 52 + '  We can change that by returning `True` from the `__exit__` method:')
#
#
class MyContext:
    def __init__(self):
        self.obj = None

    def __enter__(self):
        print('entering context...')
        self.obj = 'the Return Object'
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting context...')
        if exc_type:
            print(f'*** Error occurred: {exc_type}, {exc_val}')
        return True # suppress exceptions


with MyContext() as obj:
    return ValueError
# print('reached here without an exception...')
# # entering context...
# # exiting context...
# # *** Error occurred: <class 'ValueError'>,
# # reached here without an exception...
# # ######################################################################################################################
#
# print('#' * 52 + '  Look at the output of this code:')
#
# w___ M... a_ obj
#     print('running inside with block...')
#     print ob.
# print(obj)
# # entering context...
# # running inside with block...
# # the Return Object
# # exiting context...
# # the Return Object
#
# # Notice that the obj we obtained from the context manager, still exists in our scope after the with statement.
# # The with statement does not have its own local scope - it's not a function!
# # However, the context manager could manipulate the object returned by the context manager:
#
# print('#' * 52 + '  Notice that the `obj` we obtained from the context manager,'
#                  '  still exists in our scope after the `with` statement.')
# print('#' * 52 + '  The `with` statement does **not** have its own local scope - its not a function!')
# print('#' * 52 + '  However, the context manager could manipulate the object returned by the context manager:')
#
#
# c_ Resource
#     ___ __in___ ___ name
#         ____.name _ n..
#         ____.state _ N..
#
#
# c_ ResourceManager
#     ___ __i__ ____ name
#         ____.name _ n..
#         ____.resource _ N..
#
#     ___ __e__ ____
#         print('entering context')
#         ____.resource _ R.. ____.n..
#         ____.resource.state _ 'created'
#         r_ ____.resource
#
#     ___ __e__ ____ exc_type exc_value exc_traceback
#         print('exiting context')
#         ____.resource.state = 'destroyed'
#         i_ exc_type
#             print('error occurred')
#         r__ F..
#
#
# w___ R.. 'spam' a_ r..
#     print(_' res.name _ res.state'
# print(_' res.name _ res.state'
# # entering context
# # spam = created
# # exiting context
# # spam = destroyed
# # ######################################################################################################################
#
# # We still have access to res, but it's internal state was changed by the resource manager's __exit__ method.
# # Although we already have a context manager for files built-in to Python, let's go ahead and write our own anyways -
# # good practice.
#
# print('#' * 52 + '  We still have access to `res`, but its internal state was changed'
#                  '  by the resource managers `__exit__` method.')
# print('#' * 52 + '  Although we already have a context manager for files built-in to Python,'
#                  '  lets go ahead and write our own anyways - good practice.')
#
#
# c_ File
#     ___ __i__ ____ name mode
#         ____.n.. _ n..
#         ____.m.. _ m..
#
#     ___ __e__ ____
#         print('opening file...')
#         ____.file _ o.. ____.n.. ____.m..
#         r__ ____.fi..
#
#     ___ __e__ ____ exc_typ, exc_value exc_traceback
#         print('closing file...')
#         ____.f__.c..
#         r_ F..
#
#
# w___ F..  'test.txt' '_') a_ f
#     f.w..('This is a late parrot!')
# # opening file...
# # closing file...
# # ######################################################################################################################
#
# # Even if we have an exception inside the with statement, our file will still get closed.
# # Same applies if we return out of the with block if we're inside a function:
#
# print('#' * 52 + '  Even if we have an exception inside the `with` statement, our file will still get closed.')
# print('#' * 52 + '  Same applies if we return out of the `with` block if we are inside a function:')
#
#
# ___ test
#     w__ F.. test.txt '_') a_ f
#         f.w.. 'This is a late parrot')
#         i_ T..
#             r) f
#         print(f.cl__
#     print(f.cl__
#
#
# f _ t..
# # opening file...
# # closing file...
# # ######################################################################################################################
#
# # Note that the __enter__ method can return anything, including the context manager itself.
# # If we wanted to, we could re-write our file context manager this way:
#
# print('#' * 52 + '  Note that the `__enter__` method can return anything, including the context manager itself.')
# print('#' * 52 + '  If we wanted to, we could re-write our file context manager this way:')
#
#
# c_ File
#     ___ __i__ ____ name mode
#         ____.n.. _ n..
#         ____.m.. _ m..
#
#     ___ __e__ ____
#         print('opening file...')
#         ____.file _ o.. ____.n.. ____.m..
#         r_ ____
#
#     ___ __e__ ____ exc_type exc_value exc_traceback
#         print('closing file...')
#         ____.f__.c..
#         r_ F..
#
# # Of course, now we would have to use the context manager object's file property to get a handle to the file:
#
#
# w___ F.. test.txt '_') a_ file_ctx
#     print n..  f.._c_.fi..
#     print(fi._c__.na..
#     print(fi._c__.mo..
#
# # opening file...
# # This is a late parrot
# # test.txt
# # r
# # closing file...
