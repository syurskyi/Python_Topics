# c_ stepper:
#     ___ __getitem__ ____ i
#         r_ ____.data i
#
# X = ?                     # X is a stepper object
# X.data = "Spam"
# print('#' * 23 + ' Indexing calls __getitem__')
# print(X[1])                              # Indexing calls __getitem__
#
# print('#' * 23 + ' for loops call __getitem__')
# ___ item i_ X                    # for loops call __getitem__
#     print ?          # for indexes items 0..N
#
#
# print('#' * 23 + '  All call __getitem__ too')
# print('p' in X)                          # All call __getitem__ too
#
# print('#' * 23 + ' List comprehension')
# print([c for c in X])                    # List comprehension
#
# print('#' * 23 + '   map calls (use list() in 3.0)')
# print li..  ma.  st_.up.. ?           # map calls (use list() in 3.0)
#
#
# (a, b, c, d) = X                  # Sequence assignments
# print('#' * 23 + ' Sequence assignments')
# print(a, c, d)
#
# print('#' * 53)
# print(li.. ? tu.. ? ''.jo.. ?
#
# print('#' * 53)
# print(X)
