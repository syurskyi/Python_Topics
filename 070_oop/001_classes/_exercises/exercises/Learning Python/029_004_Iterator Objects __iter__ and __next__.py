# # You're using Python 2.x, which has used .next() since forever and still does so - only Python 3 renamed that method ' \
# # to .__next__(). Python 2 and 3 aren't compatible. If you're reading a 3.x book, use Python 3.x yourself, and vice versa.
# #
# # ___ Python 2.x, you can change __next__() to next()
#
# f__ -f ______ p._f.
# ### file: iters.py
#
# c_ Squares
#     ___ -  ____ start stop    # Save state when created
#         ____.value = s.. - 1
#         ____.stop = s..
#     ___ -i ____                 # Get iterator object on iter()
#         r_ ____
#     ___ -n  ____               # Return a square on each iteration
#         __ ____.v.. __ ____.st..     # Also called by next() built-in
#             r... S...
#         ____.v... += 1
#         r_ ____.v... ** 2
#
# print('#' * 23 + '___ calls iter(), which calls __iter__()')
# # from iters import Squares
# ___ i __ S... 1 5            # ___ calls iter(), which calls __iter__()
#     print(i, end=' ')               # Each iteration calls __next__()
#
# print('#' * 23 + 'Iterate manually: what loops do')
# X = S... 1, 5                  # Iterate manually: what loops do
# I = iter(X)                         # iter() calls __iter__
# next(I)                             # next() calls __next__
#
# next(I)
#
# next(I)
#
# # next(I)                             # Can catch this in try statement
# # # StopIteration
# #
# X = S...(1, 5)
# # X[1]
# # # AttributeError: Squares instance has no attribute '__getitem__'
# #
# print('#' * 23 + 'Exhausts items')
# X = Squares(1, 5)
# print n ___ ? __ X                # Exhausts items
# #
# print n ___ ? __ X              # Now it's empty
#
# print('#' * 23 + 'Make a new iterator object')
# print n ___ ? __ ?|1, 5    # Make a new iterator object
# #
# print(li.. ? 1, 3
# #
# #
# print('#' * 23)
# print('#' * 23)
#
# ___ gsquares start stop
#     ___ i __ ra..  s.. s..+1
#         y... i ** 2
# #
# ___ i __ ? 1, 5
#     print i e.._' '
# #
# print('#' * 23)
# print('#' * 23)
# print x ** 2 ___ ? __ ra.. 1, 6
# #
#
# print('#' * 23)
# print('#' * 23)
# S = 'ace'
# ___ x __ ?
#     ___ y __ ?
#         print ? + ? e.._' '
# #
# # ### file: skipper.py
# #
# c_ SkipIterator
#     ___ - ____ wrapped
#         ____.?  ?                  # Iterator state information
#         ____.offset  = 0
#     ___ -n ____
#         __ ____.offset >= le. ____.w..      # Terminate iterations
#             r____ S..
#         _____
#             item = ____.w... ____.o..      # else return and skip
#             ____.o.. += 2
#             r_ ?
#
# c_ SkipObject
#     ___ - ____ wrapped                # Save item to be used
#         ____.?  ?
#     ___ -i ____
#         r_ S... ____.w...         # New iterator each time
#
# __ _______ __ ______
#     alpha = 'abcdef'
#     skipper = S... ?                   # Make container object
#     I = it.. ?                             # Make an iterator on it
#     print(next(I), next(I), next(I))              # Visit offsets 0, 2, 4
# #
#     ___ x __ s..               # ___ calls __iter__ automatically
#         ___ y __ s..           # Nested fors call __iter__ again each time
#             print ? + ? e.._' ')   # Each iterator has its own state, offset
# #
# #
# print('#' * 23)
# print('#' * 23)
# print('#' * 23)
#
# S = 'abcdef'
# ___ x __ ? ;;2
#     ___ y __ ? ;;2            # New objects on each iteration
#         print(? + ? e.._' '
#
# print('#' * 23)
# print('#' * 23)
#
# S = 'abcdef'
# S = ? ::2
# print(S)
# print('#' * 23)
#
# ___ x __ ?
#     ___ y __ ?                 # Same object, new iterators
#         print ? + ? e.._' '
#
