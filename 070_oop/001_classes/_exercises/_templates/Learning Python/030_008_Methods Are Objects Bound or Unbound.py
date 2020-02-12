# c_ Spam
#     ___ doit ____ message
#         print ?
#
# print('#' * 23 + ' normal operation')
# object1 _ ?
# ?.d.. hello world22222
#
#
# print('#' * 23 + ' Bound method')
# object1 _ ?
# x _ ?.d..        # Bound method object: instance+function
# ? hello world        # Same effect as object1.doit('...')
#
#
# print('#' * 23 + ' Bound method')
# object1 _ S..
# t = S_.d..          # Unbound method object (a function in 3.0: see ahead)
# ? _1 'howdy'     # Pass in instance (if the method expects one in 3.0)
#
# print('#' * 23 + ' Class Bound method')
# c_ Eggs
#     ___ m1 ____ n
#         print(n)
#
#     ___ m2 ____
#         x _ ____.m1     # Another bound method object
#         ? 42           # Looks like a simple function
#
# ?._2             # Prints 42
