# __author__ = 'sergejyurskyj'
#
# D = di.. a 1 b 2 c 3
# print ?
#
# print('#' * 52 + ' Makes a view object in 3.0, not a list')
# K = ?.k..                       # Makes a view object in 3.0, not a list
# print ?
#
# print('#' * 52 + ' Force a real list in 3.0 if needed')
# print li.. ?                            # Force a real list in 3.0 if needed
#
# print('#' * 52 + ' Ditto for values and items views')
# V = 1?.?                     # Ditto for values and items views
# print ?
# print li.. ?
# print li.. 1?.it..
#
# print('#' * 52 + ' List operations fail unless converted')
# #K[0]                               # List operations fail unless converted
#                                     # TypeError: 'dict_keys' object does not support indexing
# print li.. ? 0
#
# print('#' * 52 + ' Iterators used automatically in loops')
# ___ k __ 1?.k.. print ?        # Iterators used automatically in loops
#
# print('#' * 52 + ' Still no need to call keys() to iterate')
# ___ key __ ? print ?           # Still no need to call keys() to iterate
#
#
# D = a 1 b 2 c 3
# print ?
#
# K = ?.k..
# V = ?.v..
#
# print('#' * 52 + ' Views maintain same order as dictionary')
# print(li.. K                # Views maintain same order as dictionary
# print(li.. V
#
# print('#' * 52 + ' Change the dictionary in-place')
# del D['b']             # Change the dictionary in-place
# print(D)
#
# print('#' * 52 + ' Reflected in any current view objects')
# print(li.. K                # Reflected in any current view objects
#
# print('#' * 52 + ' Not true in 2.X!')
# print(li.. V                # Not true in 2.X!
