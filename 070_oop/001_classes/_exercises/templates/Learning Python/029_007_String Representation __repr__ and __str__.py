# c_ adder:
#     ___ - ____ value_0
#         ____.data _ v..                   # Initialize data
#     ___ -a ____ other
#         ____.d.. += o..                   # Add other in-place (bad!)
#
# x = a...                                  # Default displays
# print('#' * 23 + '  Default displays')
# print(x)
#
#
# c_ addrepr a..                        # Inherit __init__, __add__
#     ___ -r ___                      # Add string representation
#         r_ 'addrepr(/_)'/ ____.data     # Convert to as-code string
#
# x = ? 2                              # Runs __init__
# print(x + 1)                                        # Runs __add__
# print('#' * 23 + '  Runs __repr__')
# print(x)                                            # Runs __repr__
# addrepr(3)
# print(x)                                     # Runs __repr__
# addrepr(3)
# print('#' * 23 + '  Runs __repr__ for both')
# print(str(x), repr(x))                              # Runs __repr__ for both
#
# c_ addstr a..
#     ___ -s ____                       # __str__ but no __repr__
#         r_ '[Value: /_]' / ____.data     # Convert to nice string
#
# x = a... 3
# x + 1
# print('#' * 23 + '  Default __repr__')
# x                                            # Default __repr__
# print('#' * 23 + '  Runs __str__')
# print(x)                                     # Runs __str__
#
# print(str(x), repr(x))
#
#
#
# c_ addboth a..
#     ___ -s ____
#         r_ '[Value: /_' / ____.data     # User-friendly string
#     ___ __repr__(____):
#         r_ 'addboth(/_' / ____.data     # As-code string
#
# x = ? 4
# x + 1
# x                                            # Runs __repr__
# addboth(5)
# print('#' * 23 + ' Runs __str__')
# print(x)                                     # Runs __str__
#
# print(str(x), repr(x))
#
# c_ Printer:
#     ___ - ____ val
#         ____.v.. _ v..
#     ___ -s ____                  # Used for instance itself
#         r_ st. ____.v..            # Convert to a string result
#
# objs =  ? 2  ? 3
# print('#' * 23 + ' __str__ run when instance printed')
# print('#' * 23 + ' But not when instance in a list!')
# ___ x i_ o.. print(x)                 # __str__ run when instance printed
#                                         # But not when instance in a list!
#
#
# print(objs)
# # # [<__main__.Printer object at 0x025D06F0>, <__main__.Printer object at ...more...
# # objs
# # # [<__main__.Printer object at 0x025D06F0>, <__main__.Printer object at ...more...
#
#
#
# c_ Printer
#     ___ - ____ val
#         ____.v.. _ v..
#     ___ -r ____                 # __repr__ used by print if no __str__
#         r_ st. ____.v..            # __repr__ used if echoed or nested
#
# objs =  ? 2 ? 3
# print('#' * 23 + ' No __str__: runs __repr__')
# ___ x i_ ? print(x)                 # No __str__: runs __repr__
# #
# #
# #
# print('#' * 23 + ' Runs __repr__, not ___str__')
# print(objs)                             # Runs __repr__, not ___str__
# #
# # objs
