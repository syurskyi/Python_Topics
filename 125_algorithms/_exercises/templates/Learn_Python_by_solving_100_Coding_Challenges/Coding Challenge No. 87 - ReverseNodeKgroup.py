# # Reverse Nodes in k-Group
# # Question: Given a linked list, reverse the nodes of a linked list k at a time and return its modified list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is. You may not alter the values in the nodes, only nodes itself may be changed. Only constant memory is allowed.
# # For example,
# # Given this linked list: 1->2->3->4->5
# # For k = 2, you should return: 2->1->4->3->5
# # For k = 3, you should return: 3->2->1->4->5.
# # Solutions:
#
#
# c_ ListNode object
#     ___  -  x
#         val _ x
#         next _ N..
#
#     ___ to_list
#         r_  v.. + n__.t..  __ ? ____ v..
#
#
# c_ Solution object
#     ___ reverseKGroup  head k
#         """
#         :type head: ListNode
#         :type k: i..
#         :rtype: ListNode
#         """
#         __ no. ? o. ? <_ 1
#             r_ ?
#         dummy _ ? -1
#         ?.n.. _ h..
#         temp _ ?
#         w___ ?
#             t.. _ ? ? ?
#         r_ ?.n..
#
#     ___ reverseNextK  head k
#         # Check if there are k nodes left
#         temp _ ?
#         ___ i __ ra.. ?
#             __ no. ?.n..
#                 r_ N..
#             t.. _ ?.n..
#
#         # The last node when the k nodes reversed
#         node _ h__.n..
#         prev _ h..
#         curr _ h__.n..
#         # Reverse k nodes
#         ___ i __ ra.. k
#             nextNode _ c__.n..
#             c__.n.. _ p..
#             p.. _ c..
#             c.. _ n..
#         # Connect with head and tail
#         n__.n.. _ c..
#         h__.n.. _ p..
#         r_ node
#
#
# __  -n __ _____
#     n1 _ ? 1
#     n2 _ ? 2
#     n3 _ ? 3
#     n4 _ ? 4
#     n5 _ ? 5
#     n1.n.. _ n2
#     n2.n.. _ n3
#     n3.n.. _ n4
#     n4.n.. _ n5
#     r _ ? .? n1 3
#     print   ?.t..