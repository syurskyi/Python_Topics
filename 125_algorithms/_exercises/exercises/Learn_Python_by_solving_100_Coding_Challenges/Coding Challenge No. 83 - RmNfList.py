# # Remove Nth Node from End of List
# # Question: Given a linked list, remove the nth node from the end of list and return its head.
# # For example:
# # Given linked list: 1->2->3->4->5, and n = 2.
# # After removing the second node from the end, the linked list becomes 1->2->3->5.
# # Note: Given n will always be valid. Try to do this in one pass.
# # Solutions:
#
#
# c_ ListNode
#     ___  -  x
#         val _ ?
#         next _ N..
#
#
# c_ Solution
#     ___ getlength head
#         res _ 0
#         w___ ?
#             ? +_ 1
#             h.. _ ?.n..
#         r_ ?
#
#     ___ removeNthFromEnd  head n
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         __ getlength head__n
#             r_ ?.n..
#
#         node _ h..
#         ___ i __ ra.. ? h.. - ? - 1
#             n.. _ ?.n..
#         n__.n.. _ ?.n__.n..
#         r_ ?
#
#     ___ printll node
#         w___ ?
#             print ?.v..
#             ? _ ?.n..
#
#
# __  -n __ ______
#     ll1 ?.n.. ?.n__.n.. _ ? 0, ? 1, ? 5
#     ? .p..  ? .? ? 2