# c_ HashTable o..
#
#     ___ -
#         size _ 10
#         keys _ |N.. * s..
#         values _ |N.. * s..
#
#     ___ put key data
#
#         index _ h.. ?
#
#         # not None -> it is a collision !!!
#         w___ k..|? __ no. N..
#             __ k..|i.. __ k..
#                 v..|i.. _ d.  # update
#                 r_
#
#             # rehash try to find another slot
#             i.. _ ? + 1) % s..
#
#         # insert
#         k..|? _ k..
#         v..|i.. _ d..
#
#     ___ get key
#
#         index _ h.. ?
#
#         w___ k..|? i. no. N..
#             __ k..|i.. __ k..
#                 r_ v..|i..
#
#             i.. _ ? + 1) % s..
#
#         # it means the key is not present in the associative array
#         r_ N..
#
#     ___ hashfunction key
#         sum _ 0
#         ___ pos __ ra.. le. ?
#             s.. _ ? + or.|k..|?
#
#         r_ ? % ?
#
#
# __ ______ __ _____
#     table _ ?
#
#     ?.p.. "apple", 10
#     ?.p.. "orange", 20
#     ?.p.. "car", 30
#     ?.p.. "?", 40
#
#     print(?.g.. "cara"
