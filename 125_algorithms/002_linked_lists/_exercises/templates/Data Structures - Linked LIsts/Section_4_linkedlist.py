# c_ Node o..
#
#     ___  -  data
#         ?  ?
#         nextNode _ N..
#
#
# c_ LinkedList o..
#
#     ___  -
#         head _ N..
#         size _ 0
#
#     # O(1) !!!
#     ___ insertStart  data
#
#         size _ s.. + 1
#         newNode _ N.. ?
#
#         __ no. h..
#             h.. _ nN..
#         ____
#             nN.nextNode _ h..
#             h.. _ nN..
#
#     ___ remove data
#
#         __ h.. i. N..
#             r_
#
#         s.. _ s.. - 1
#
#         currentNode _ h..
#         previousNode _ N..
#
#         w____ cN__.d.. !_ d...
#             pN__ _ cN__
#             cN__ _ cN__.nN..
#
#         __ pN__ __ N..
#             head _ cN__.nN..
#         ____:
#             pN__.nN.. _ cN__.nN..
#
#     # O(1)
#     ___ size1 ____
#         r_ s..
#
#     # O(N) no. good !!!
#     ___ size2
#
#         actualNode _ h..
#         size _ 0
#
#         w____ aN.. __ no. N..
#             s.. +_ 1
#             aN.. _ aN__.nN..
#
#         r_ ?
#
#     # O(N)
#     ___ insertEnd data
#
#         s.. _ s.. + 1
#         newNode _ N.. ?
#         actualNode _ h..
#
#         w____ aN__.nN.. __ no. N..
#             aN__ _ aN__.nN..
#
#         aN__.nN.. _ newNode
#
#     ___ traverseList ____
#
#         actualNode _ head
#
#         w___ aN__ __ no. N..
#             print("@ "  aN__.d..
#             aN__ _ aN__.nN..
#
#
# linkedlist _ L..
#
# ?.iS.. 12
# ?.iS.. 122
# ?.iS.. 3
# ?.iE.. 31
#
# ?.t..
#
# ?.r.. 3
# ?.r.. 12
# ?.r.. 122
# ?.r.. 31
#
# print ?.size1
