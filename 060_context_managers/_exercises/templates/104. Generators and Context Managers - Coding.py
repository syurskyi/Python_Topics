# # Generators and Context Managers
# # Let's see how we might write something that almost behaves like a context manager, using a generator function:
#
# print('#' * 52 + '  ### Generators and Context Managers')
#
#
# ___ my_gen
#     t__
#         print('creating context and yielding object')
#         lst _ 1 2 3 4 5
#         y___ l..
#     f___
#         print('exiting context and cleaning up')
#
#
# gen _ m..  # create generator
#
# lst _ n.. g..  # enter context and get "as" object
# print l..
# # [1, 2, 3, 4, 5]
# # ######################################################################################################################
#
# # next(gen)  # exit context    # StopIteration:
#
# # As you can see, the exiting context code ran. But to make this cleaner, we'll catch the StopIteration exception:
#
# print('#' * 52 + '  As you can see, the exiting context code ran.')
# print('#' * 52 + '  But to make this cleaner, we will catch the StopIteration exception:')
#
# gen _ m..
# lst _ n.. g..
# print l..
# t__
#     n.. g..
# e_____ S..I..
#     p____
# # creating context and yielding object
# # [1, 2, 3, 4, 5]
# # exiting context and cleaning up
# # ######################################################################################################################
#
#
# # Now let's write a context manager that can use the type of generator we wrote so we can use it using a with statement
# # instead:
# print('#' * 52 + '  Now lets write a context manager that can use the type of generator we wrote'
#                  '  so we can use it using a `with` statement instead:')
#
#
# c_ GenCtxManager
#     ___ __i__ ____ gen_func
#         ____._gen _ g.._f.
#
#     ___ __e__ ____
#         r_ n.. ____._g..
#
#     ___ __e__ ____ exc_type exc_value exc_tb
#         t__
#             n.. ____._g..
#         e___ S..I..
#             p___
#         r_ F..
#
#
# w__ G.. m._g. a_ lst
#     print l..
# # creating context and yielding object
# # [1, 2, 3, 4, 5]
# # exiting context and cleaning up
# # ######################################################################################################################
#
# # Our GenCtxManager class is not very flexible - we cannot pass arguments to the generator function for example.
# # We are also not doing any exception handling...
# # We could try some of this ourselves. For example handling arguments:
#
# print('#' * 52 + '  Our `GenCtxManager` class is not very flexible -'
#                  '  we cannot pass arguments to the generator function for example.')
# print('#' * 52 + '  We are also not doing any exception handling...')
#
#
# c_ GenCtxManager
#     ___ __i__ ____ gen_func 0a.. 00k..
#         ____._gen _ g._f. 0a.. 00k..
#
#     ___ __e__ ____
#         r_ n.. ____._g..
#
#     ___ __e__ ____ exc_type exc_value exc_tb
#         t__
#             n.. ____._g..
#         e_____ S..I..
#             p___
#         r_ F..
#
#
# ___ open_file fname mode
#     t__
#         print('opening file...')
#         f _ o.. f.. m..
#         y____ f
#     f_____
#         print('closing file...')
#         f.c..
#
#
# w__ G... open_file test.txt '_') a_ f
#     print('writing to file...')
#     f.w.. 'testing...'
# # opening file...
# # writing to file...
# # closing file...
# # ######################################################################################################################
#
# print('#' * 52 + '  ')
#
# w.. o.. test.txt a_ f
#     print n.. f
# # testing...
# # ######################################################################################################################
#
# # This works, but is not very elegant, and we still are not doing much exception handling. In the next video,
# # we'll look at a decorator in the standard library that does this far more robustly and elegantly...
#
