# # Remove Duplicates from Sorted List
# # Question: Given a sorted linked list, delete all duplicates such that each element appear only once.
# # For example:
# # Given 1->1->2, return 1->2.
# # Given 1->1->2->3->3, return 1->2->3.
# # Solutions:
#
#
# c_ ListNode
#     ___  -  x
#         val _ x
#         next _ N..
#
#
# c_ Solution
#     # @param head, a ListNode
#     # @return a ListNode
#     ___ deleteDuplicates  head
#         __ ? __ N.. o. ?.n.. __ N..
#             r_ ?
#         p _ ?
#         w___ p.n..
#             __ p.v.. __ p.n...v..
#                 p.n.. _ p.n...n..
#             ____
#                 p _ p.n..
#         r_ ?
#
#     ___ printll  node
#         w___ ?
#             print   ?.v..
#             ? _ ?.n..
#
#
# __  -n __ ______
#     ll1 ?.n.. ?.n...n.. _ ? 2 ? 2 ? 5
#     > .p.. ? .d.. ?