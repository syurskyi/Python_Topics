# c_ Commuter:
#     ___ - ____, val
#         ____.v.. _ v..
#
#     ___ -a ____ other
#         print('add', ____.v.., o...
#         r_ ____.v.. + o...
#
#     ___ -ra ____ other
#         print('radd', ____.v.., o...)
#         r_ o... + ____.v..
#
# x = ? 88
# y = ? 99
#
# print('#' * 23 + ' __add__: instance + noninstance')
# x + 1                         # __add__: instance + noninstance
# # add 88 1
#
# print('#' * 23 + ' __radd__: noninstance + instance')
# 1 + y                         # __radd__: noninstance + instance
# # radd 99 1
#
# print('#' * 23 + ' __add__: instance + instance, triggers __radd__')
# x + y                         # __add__: instance + instance, triggers __radd__
#
#
# c_ Commuter                        # Propagate c_ type in results
#     ___ -____, val
#         ____.v.. _ v..
#
#     ___ -a ____ other
#         i_ isi.... o... C...  o... _ o....v..
#         r_ C... ____.v.. + o...
#
#     ___ -ra.. ____ other
#         r_ C... o... + ____.v..
#
#     ___ -s ____
#         r_ '<Commuter: /_>' / ____.v..
#
# x = ? 88
# y = ? 99
# print('#' * 23 + ' Result is another Commuter instance')
# print(x + 10)                          # Result is another Commuter instance
#
# print(10 + y)
#
#
# z = x + y                              # Not nested: doesn't recur to __radd__
# print('#' * 23 + ' Not nested: doesnt recur to __radd__')
# print(z)
#
# print(z + 10)
# print(z + z)
#
#
# c_ Number
#     ___ -____ val
#         ____.v.. _ v..
#
#     ___ -ia ____ other             # __iadd__ explicit: x += y
#         ____.v.. +_ o...                  # Usually returns ____
#         r_ ____
#
# print('#' * 23 + '  __iadd__ explicit: x += y')
# print('#' * 23 + ' Usually returns ____')
# x = ? 5
# x += 1
# x += 1
# print(x.v..)
#
#
# c_ Number
#     ___ -____, val
#         ____.v.. _ v..
#
#     ___ -a ____ other              # __add__ fallback: x = (x + y)
#         r_ N.. ____.v.. + o...    # Propagates c_ type
#
# print('#' * 23 + ' __add__ fallback: x = (x + y)')
# print('#' * 23 + ' Propagates c_ type')
# x = ? 5
# x += 1
# x += 1
# print(x.v..)
