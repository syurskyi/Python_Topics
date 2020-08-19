# c_ Node
#     ___  -  data
#         .data _ ?
#         .prev _ N..
#         .n.. _ N..
#
#
# c_ LinkedList
#     ___  -
#         .h.. _ N..
#
#     ___ createList arr
#         start _ .h..
#         n _ le. ?
#
#         temp _ start
#         i _ 0
#
#         w___ ? < ?
#             newNode _ N.. a.. ?
#             __ i __ 0
#                 start _ n..
#                 temp _ ?
#             ____
#                 t__.n.. _ n..
#                 n__.p.. _ t__
#                 temp _ t__.n..
#             i +_ 1
#         .h.. _ s..
#         r_ ?
#
#     ___ printList
#         temp _ .h..
#         linked_list _ ""
#         w___ t..
#             ? +_  st. t__.d.. + " "
#             temp _ t__.n..
#
#         print ?
#
#     ___ countList
#         temp _ .h..
#         count _ 0
#         w___ t.. pa__ no. N..
#             temp _ t__.n..
#             c.. +_ 1
#         r_ ?
#
#     # we will consider that the index begin at 1
#     ___ insertAtLocation value index
#         temp _ .h..
#
#         count _ .c..
#
#         #index is 6, count is 5, valid
#         #index is 7, count is 5,
#         __ c.. + 1< i..
#             r_ t..
#
#         newNode _ N.. v..
#
#         __ index __ 1
#             n__.n.. _ t..
#             temp.p.. _ n..
#             .h.. _ n..
#             r_ .h..
#
#         __ i.. __ c.. +1
#             w___ t__.n.. pa__ no. N..
#                 temp _ t__.n..
#
#             t__.n.. _ n..
#             n__.p.. _ t..
#             r_ .h..
#
#         i _ 1
#         w___ ? < i.. - 1
#             temp _ t__.n..
#             ?+_1
#
#         nodeAtTarget _ t__.n..
#
#         n__.n.. _ ?
#         ?.p.. _ n..
#
#         t__.n.. _ n..
#         n__.p.. _ t..
#
#         r_ .h..
#
#
# arr _ [1, 2, 3, 4, 5]
#
# llist _ ?
#
# ?.c.. ?
#
# ?.i.. 5 6
#
# ?.p..
