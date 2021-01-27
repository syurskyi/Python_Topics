# c_ Node:
#     ___  -   value_N.. next_N.. prev_N..
#         ? _ ?
#         ? _ ?
#         ? _ ?
#
#
# c_ LinkedList
#     ___  -
#         head _ N..
#
#     ___ insert
#         p..
#
#     ___ delete
#         p..
#
#     # Traverse Method To Print All Elements #
#     ___ traverse
#         node _ h..
#         w__ ? __ no. N..
#             print ?.v..
#             node _ ?.n..
#
#
# n1 = Node(3)
# n2 = Node(7)
# n3 = Node(2)
# n4 = Node(9)
#
# LL = LinkedList()
# LL.head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
#
# # Traverse Method To Print All Elements #
# LL.traverse()