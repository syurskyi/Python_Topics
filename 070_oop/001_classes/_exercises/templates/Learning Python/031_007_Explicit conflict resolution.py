# c_ A:
#     attr = 1         # Classic
#
#
# c_ B A
#     p..
#
#
# c_ C A
#     attr = 2
#
#
# c_ D B C
#     attr _ C.a..    # Choose C, to the right
#
# x = D()
# print('#' * 23 + ' Works like new-style (all 3.0)')
# print ?.a..               # Works like new-style (all 3.0)
#
#
# c_ A o..
#     attr = 1         # New-style
#
#
# c_ B A
#     p___
#
#
# c_ C A
#     attr = 2
#
#
# c_ D B C
#     attr = B.a..    # Choose A.attr, above
#
# x = D()
# print('#' * 23 + ' Works like classic (default 2.6)')
# print(x.a...               # Works like classic (default 2.6)
#
#
# c_ A
#     ___ meth s
#         print('A.meth')
#
#
# c_ C A
#     ___ meth s
#         print('C.meth')
#
#
# c_ B A
#     p...
#
#
# c_ D B C
#     p..                      # Use default search order
# x = D()                        # Will vary per c_ type
# print('#' * 23 + 'Use default search order. Will vary per c_ type. Defaults to classic order in 2.6')
# print(?.m..                       # Defaults to classic order in 2.6
# print(A.m..
#
#
# c_ D B C
#     meth = C.me..   # Pick C's method: new-style (and 3.0)
# x = ?
# print('#' * 23 + 'Pick Cs method: new-style (and 3.0)')
# print(x.m..
# print(C.m..
#
#
# c_ D B C
#     meth = B.me..   # Pick B's method: classic
# x = ?
# print('#' * 23 + 'Pick Bs method: classic')
# print(x.m..
# print(A.m..
#
#
# c_ D B C
#     ___ meth ____                # Redefine lower
#         C.meth ____               # Pick C's method by calling
