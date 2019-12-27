# c_ C
#     data _ 'spam'                          # 2.6 only
#     ___ __cmp__ ____ other              # __cmp__ not used in 3.0
#         r_ ? ____.d.. o..     # cmp() not defined in 3.0
#
# X = ?
# print('#' * 23 + ' True  (runs __cmp__)')
# print(X > 'ham')         # True  (runs __cmp__)
# print('#' * 23 + ' False (runs __cmp__)')
# print(X < 'ham')         # False (runs __cmp__)
#
#
#
# c_ C
#     data = 'spam'
#     ___ __cmp__ ____ other
#         r_ ____.d.. > o.. - ____.d... < o...
