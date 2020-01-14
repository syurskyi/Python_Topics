# # You should be familiar with try and finally.
# #
# # We use the finally block to make sure a piece of code is executed, whether an exception has happened or not:
#
# print('#' * 52 + '  You should be familiar with `try` and `finally`.')
#
# t__
#     10 / 2
# _____ Z.....
#     print('Zero division exception occurred')
# f____
#     print('finally ran!')
#
# print('#' * 52 + '  ')
#
# # finally ran!
#
# ___
#     1 / 0
# ______ Z.....
#     print('Zero division exception occurred')
# f____
#     print('finally ran!')
#
# print('#' * 52 + '  You will see that in both instances, the `finally` block was executed.'
#                  '  Even if an exception is raised in the `except` block, the `finally` block will **still** execute!')
#
# print(
#     '#' * 52 + 'Even if the finally is in a function and there is a return statement in the `try` or `except` blocks:')
#
# # Zero division exception occurred
# # finally ran!
# # ######################################################################################################################
# # You'll see that in both instances, the finally block was executed. Even if an exception is raised in the except block,
# # the finally block will still execute!
# # Even if the finally is in a function and there is a return statement in the try or except blocks:
#
#
# ___ my_func
#     ___
#         1 / 0
#     ______
#         r_
#     _____
#         print('finally running...')
#
#
# my_func()
#
# print('#' * 52 + '  This is very handy to release resources even in cases where an exception occurs. ')
# print('#' * 52 + '  For example making sure a file is closed after being opened:')
#
# ___
#     f _ o.. test.txt _
#     a _ 1 / 0
# _____
#     print('an exception occurred...')
# f____
#     print('Closing file...')
#     f.c...
#
# # We should always do that when dealing with files.
# # But that can get cumbersome...
# # So, there is a better way.
# # Let's talk about context managers, and the pattern we are trying to solve:
# #     Run some code to create some object(s)
# #     Work with object(s)
# #     Run some code when done to clean up object(s)
# # Context managers do precisely that.
# # We use a context manager to create and clean up some objects. The key point is that the cleanup needs to happens
# # automatically - we should not have to write code such as the try...except...finally code we saw above.
# # When we use context managers in conjunction with the with statement, we end up with the "cleanup" phase happening as
# # soon as the with statement finishes:
#
#
# print('#' * 52 + '  We should **always** do that when dealing with files.')
# print('#' * 52 + '  ')
# print('#' * 52 + '  When we use context managers in conjunction with the `with` statement,'
#                  '  we end up with the "cleanup" phase happening as soon as the `with` statement finishes:')
#
# w___ o.. 'test.txt' _ a_ f..
#     print('inside with: file closed?' ?.cl..
# print('after with: file closed?', ?.cl__)
# # inside with: file closed? False
# # after with: file closed? True
# # ######################################################################################################################
#
# print('#' * 52 + '  This works even in this case:')
#
#
# ___ test
#     w___ o.. 'test.txt' _ __ ....
#         print('inside with: file closed?', ?.cl__)
#         r_ ?
#
# # As you can see, we return directly out of the with block...
#
#
# file = ?
# # inside with: file closed? False
#
# print(?.cl__)
# # True
#
# print('#' * 52 + '  And yet, the file was still closed.')
# print('#' * 52 + '  It also works even if we have an exception in the middle of the block')
# # with open('test.txt', 'w') as f:
# #     print('inside with: file closed?', f.closed)
# #     raise ValueError()                              ###### ValueError:
# # ######################################################################################################################
#
# print('after with: file closed?', f.cl__)
# # after with: file closed? True
#
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
#
# # Context managers can be used for more than just opening and closing files.
# # If we think about it there are two phases to a context manager:
# #     when the with statement is executing: we enter the context
# #     when the with block is done: we exit the context
# # We can create our own context manager using a class that implements an __enter__ method which is executed when
# # we enter the context, and an __exit__ method that is executed when we exit the context.
# # There is a general pattern that context managers can help us deal with:
# #     Open - Close
# #     Lock - Release
# #     Change - Reset
# #     Enter - Exit
# #     Start - Stop
# # The __enter__ method is quite straightforward. It can (but does not have to) return one or more objects we then
# # use inside the with block.
# # The __exit__ method however is slightly more complicated.
# #     It needs to return a boolean True/False. This indicates to Python whether to suppress any errors that occurred
# #     in the with block. As we saw with files, that was not the case - i.e. it returns a False
# #     If an error does occur in the with block, the error information is passed to the __exit__ method - so it needs
# #     three things: the exception type, the exception value and the traceback. If no error occured, then those values
# #     will simply be None.
# #
# # We haven't covered exceptions in detail yet, so let's quickly see what those three things are:
#
#
# # ___ my_func
# #     return 1.0 / 0.0
# # my_func()  # Z.....: float division by zero
# # ######################################################################################################################
#
# print('#' * 52 + '  Lets go ahead and create a context manager:')
#
# # The exception type here is Z......
# # The exception value is float division by zero.
# # The traceback is an object of type traceback (that itself points to other traceback objects forming the trace stack)
# # used to generate that text shown in the output.
# # I am not going to cover traceback objects at this point - we'll do this in a future part (OOP) of this series.
# # Let's go ahead and create a context manager:
#
#
# c_ MyContext
#     ___ - ____
#         ____.obj _ N...
#
#     ___ -e ____
#         print('entering context...')
#         ____.o.. _ 'the Return Object'
#         r__ ____.?
#
#     ___ -e ____ __ __
#         print('exiting context...')
#         i_ e_t..
#             print _'*** Error occurred: |e_t.. e_v
#         r_ F..  # do not suppress exceptions
#
# # with MyContext() as obj:
# #     raise ValueError    # ValueError:
#
#
# # As you can see, the __exit__ method was still called - which is exactly what we wanted in the first place. Also,
# # the exception that was raise inside the with block is seen.
# # We can change that by returning True from the __exit__ method:
#
#
# print('#' * 52 + '  As you can see, the `__exit__` method was still called -'
#                  '  which is exactly what we wanted in the first place.')
# print('#' * 52 + '   Also, the exception that was raise inside the `with` block is seen.')
# print('#' * 52 + '  We can change that by returning `True` from the `__exit__` method:')
#
#
# c_ MyContext
#     ___ -
#         ____.obj _ None
#
#     ___ -e _____
#         print('entering context...')
#         ____.o.. _ 'the Return Object'
#         r_ ____.?
#
#     ___ -e
#         print('exiting context...')
#         __ e_t..
#             print(_'*** Error occurred: e_t.. e_v..
#         r_ T.. # suppress exceptions
#
#
# w___ ? __ ob.
#     r____ V..
# print('reached here without an exception...')
# # entering context...
# # exiting context...
# # *** Error occurred: <class 'ValueError'>,
# # reached here without an exception...
# # ######################################################################################################################
#
# print('#' * 52 + '  Look at the output of this code:')
#
# w___ ? __ obj
#     print('running inside with block...')
#     print ?
# print ?
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
#     ___ - ___ name
#         ____.? _ ?
#         ____.state _ N..
#
#
# c_ ResourceManager
#     ___ - ____ name
#         ____.? _ ?
#         ____.resource _ N..
#
#     ___ -e ____
#         print('entering context')
#         ____.r.. _ R.. ____.n..
#         ____.r__.st.. _ 'created'
#         r_ ____.r..
#
#     ___ -e ____ __
#         print('exiting context')
#         ____.r__.st.. = 'destroyed'
#         __ e_t..
#             print('error occurred')
#         r__ F..
#
#
# w___ R.. 'spam' __ res
#     print(_' ?.n.. _ ?.st..'
# print(_' ?.n.. _ ?.s..'
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
#     ___ ? ____ name mode
#         ____.? _ ?
#         ____.? _ ?
#
#     ___ -e
#         print('opening file...')
#         ____.file _ o.. ____.n.. ____.m..
#         r__ ____.fi..
#
#     ___ -e _____ __
#         print('closing file...')
#         ____.f__.c..
#         r_ F..
#
#
# w___ ?  'test.txt' _ __ f
#     ?.w..('This is a late parrot!')
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
#     w__ ? test.txt _ __ f
#         ?.w.. 'This is a late parrot')
#         __ T..
#             r_ ?
#         print(?.cl__
#     print(?.cl__
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
#     ___ - ____ name mode
#         ____.? _ ?
#         ____.? _ ?
#
#     ___ -e
#         print('opening file...')
#         ____.file _ o.. ____.n.. ____.m..
#         r_ ____
#
#     ___ -e ____
#         print('closing file...')
#         ____.f__.c..
#         r_ F..
#
# # Of course, now we would have to use the context manager object's file property to get a handle to the file:
#
#
# w___ ? test.txt _ __ file_ctx
#     print n..  ?.fi..
#     print(fi._c__.na..
#     print(fi._c__.mo..
#
# # opening file...
# # This is a late parrot
# # test.txt
# # r
# # closing file...
