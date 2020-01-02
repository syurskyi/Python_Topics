#
# D = dict(a=1, b=2, c=3)
# K = D.keys()
# V = D.values()
#
# print K @ x 4           # Keys (and some items) views are set-like
#
# """
# V & {'x': 4}
# # TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict'
# V & {'x': 4}.values()
# # TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict_values'
# """
#
# D = {'a':1, 'b':2, 'c':3}
#
# print('#' * 52 + ' Intersect keys views')
# print ?.k.. @ ?.k..                        # Intersect keys views
#
# print('#' * 52 + ' Intersect keys and set')
# print ?.k.. @  b'                          # Intersect keys and set
#
# print('#' * 52 + ' Intersect keys and dict')
# print ?.k.. @ 'b' 1                     # Intersect keys and dict
#
# print('#' * 52 + ' Union keys and set')
# print ?.k.. @ 'b' 'c' 'd'                 # Union keys and set
#
# D = {'a': 1}
# print('#' * 52 + ' Items set-like if hashable')
# print(li.. ?.it..                            # Items set-like if hashable
#
# print('#' * 52 + ' Union view and view')
# print ?.it.. @ ?.k..                       #  Union view and view
#
# print('#' * 52 + ' dict treated same as its keys')
# print ?.it.. @ ?                              # dict treated same as its keys
#
# print('#' * 52 + ' Set of key/value pairs')
# print ?.it.. @  'c', 3) ('d', 4           # Set of key/value pairs
#
# print('#' * 52 + ' dict accepts iterable sets too')
# print(di.. ?.it.. @ 'c', 3), ('d', 4     # dict accepts iterable sets too
