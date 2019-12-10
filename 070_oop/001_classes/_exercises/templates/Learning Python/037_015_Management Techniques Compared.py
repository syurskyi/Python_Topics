# # 2 dynamically computed attributes with properties
#
#
# c_ Powers:
#     ___ -i ____ square cube
#         ____._s.. _ s...                      # _square is the base value
#         ____._c.. _ cube                        # square is the property name
#
#     ___ getSquare ____
#         r_ ____._s.. ** 2
#
#     ___ setSquare ____ value
#         ____._s.. _ value
#     square _ pr___ g... s..
#
#     ___ getCube ____
#         r_ ____._c.. ** 3
#     cube = pr_ g...
#
#
# X = ? 3, 4
# print ?.s...      # 3 ** 2 = 9
# print ?.cube)        # 4 ** 3 = 64
# ?.s... = 5
# print ?.s...)      # 5 ** 2 = 25
#
# # Same, but with descriptors
#
#
# c_ DescSquare
#     ___ -g ____ instance owner
#         r_ i___._s.. ** 2
#
#     ___ -s ____ instance value
#         i___._s.. _ v..
#
#
# c_ DescCube
#     ___ -g  ____ instance owner
#         r_ i___._c.. ** 3
#
#
# c_ Powers                                  # Use (object) in 2.6
#     square _ D.S.
#     cube _ D.C.
#
#     ___ - ____ square cube
#         ____._s.. _ s...                  # "____.square = square" works too,
#         ____._c.. _ cube                    # because it triggers desc __set__!
#
#
# X = P.. 3 4
# print ?.s...     # 3 ** 2 = 9
# print ?.c...       # 4 ** 3 = 64
# ?.s... = 5
# print ?.s...      # 5 ** 2 = 25
#
#
# # Same, but with generic __getattr__ undefined attribute interception
#
# c_ Powers
#     ___ - ____ square cube
#         ____._s.. _ s...
#         ____._c.. _ cube
#
#     ___ -g ____ name
#         i_ n.. __ 'square'
#             r_ ____._s.. ** 2
#         e____ n.. __ 'cube':
#             r_ ____._c.. ** 3
#         e____
#             r____ T... unknown attr:' + n...
#
#     ___ -s ____ name value
#         i_ n.. __ 'square'
#             ____. -d '_s..' _ v..
#         e____
#             ____. -d n.. _ v..
#
#
# X = P.. 3 4
# print ?.sq..      # 3 ** 2 = 9
# print ?.cu..        # 4 ** 3 = 64
# ?.sq.. _ 5
# print ?.sq...      # 5 ** 2 = 25
#
#
# # Same, but with generic __getattribute__ all attribute interception
#
# c_ Powers
#     ___ - ____ square cube
#         ____._s.. _ s..
#         ____._c..   _ c..
#
#     ___ -g ____ name
#         i_ n.. __ 'square'
#             r___ obj___. -g ____ '_s..') ** 2
#         e____ n.. __ 'cube'
#             r_ obj____. -g ____ '_c..') ** 3
#         e____
#             r_ obj__. -g ____ n..
#
#     ___  s ____ name value
#         i_ n.. __ 'square'
#             ____. -d '_s..' _ v..
#         e...
#             ____. -d n.. _ v...
#
#
# X = P... 3 4
# print ?.sq..      # 3 ** 2 = 9
# print ?.cu..        # 4 ** 3 = 64
# ?.sq.. _ 5
# print ?.squ..      # 5 ** 2 = 25
