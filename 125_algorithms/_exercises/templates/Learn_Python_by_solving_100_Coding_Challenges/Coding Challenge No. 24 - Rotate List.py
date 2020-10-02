# # Rotate List
# # Question: Given a list, rotate the list to the right by k places, where k is non-negative.
# # For example:
# # Given 1->2->3->4->5->NULL and k = 2,
# # return 4->5->1->2->3->NULL
# # Solutions:
#
# c_ ListNode object
#     ___  -  x
#         val _ x
#         next _ N..
#
#     ___ to_list
#         r_ ? + ?.to_list  __ ? ____ ?
#
# c_ Solution:
#     # @param head, a ListNode
#     # @param k, an integer
#     # @return a ListNode
#     ___ rotateRight head k
#         __ ? __ N..
#             r_ N..
#         temp _ ?
#         ___ i __ ra.. 0 ?
#             __ ?.n.. __ N..
#                 t.. _ h..
#             ____
#                 t.. _ ?.n..
#         newLast _ ?
#         w___ t__.n.. !_ N..
#             t.. _ ?.n..
#             n.. _ ?.n..
#         t__.n.. _ h..
#         newHead _ n__.n..
#         n__.n.. _ N..
#         r_ ?
#
#
# __  -n __ "__main__":
#     n1 _ ? 1
#     n2 _ ? 2
#     n3 _ ? 3
#     n4 _ ? 4
#     n5 _ ? 5
#     n1.n.. _ n2
#     n2.n.. _ n3
#     n3.n.. _ n4
#     n4.n.. _ n5
#     r _ ? .? n1, 2
#     print   ?.to_list