# c_ Node
#     val _ 0
#     left _ 0
#     right _ 0
#     ___ - val
#         ? ?
#
# c_ BST
#
#     ___ - val
#         root _ ? ?
#
#     ___ insert val node
#         __ n__.v.. < ?
#             __ n__.r..
#                 #go right
#                 i.. ? n__.r..
#             _____
#                 n__.r.. _ ? ? #insert
#         ____ ? < n__.v..
#             __ n__.l..
#                 #go left
#                 i.. ? n__.l..
#             _____
#                 n__.l.. _ ? ?
#         _____
#             print ? " Already in tree")
#
#     ___ number_of_leaves  node
#         __ ?.l.. an. ?.r..
#             r_ ? ?.l..| + ? ?.r..
#         ____ ?.l..
#             r_ ? ?.l..
#         ____ ?.r..
#             r_ ? ?.r..
#         _____
#             #leave
#             r_ 1
#
#     ___ number_of_leaves_i
#         leaves _ 0
#         nodes _ |r..
#         w__ n..
#             ? _ n..|0
#             __ ?.l..
#                 n__.ap.. ?.l..
#             __ ?.r..
#                 n__.ap.. ?.r..
#             __ no. ?.l.. an. no. ?.r..
#                 l.. +_ 1
#             de. n..|0
#         r_ ?
#
#     ___ height node
#         __ ?.l.. an. ?.r..
#             print(?.v.. " Height of left ", h.. ?.l.. " Hegiht of right ", h.. ?.r..
#             r_ 1 + ma. h.. ?.l.. h.. ?.r..
#         ____ ?.l..
#             #print(?.val, height(?.left))
#             r_ 1 + h.. ?.l..
#         ____ ?.r..
#             #print(?.val, height(?.right))
#             r_ 1 + h.. ?.r..
#         _____
#             #print(?.val)
#             r_ 1
#
#     ___ is_identical second_root
#         nodes1 _ |r..
#         nodes2 _ |?
#         w__ _1 an. _2
#             ? _ _1|0
#             _2 _ _2|0
#             __ ?.v.. __ _2.v..
#                 __ ?.l..
#                     _1.ap.. ?.l..
#                 __ ?.r..
#                     _1.ap.. ?.r..
#                 __ _2.l..
#                     nodes2.ap.. _2.l..
#                 __ node2.r..
#                     _2.ap.. _2.r..
#             _____
#                 r_ F..
#             de. -1|0
#             de. -2|0
#         r_ le. _1 __ le. _2