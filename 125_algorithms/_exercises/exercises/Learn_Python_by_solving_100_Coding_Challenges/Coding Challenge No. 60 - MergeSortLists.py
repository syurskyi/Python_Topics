# # Merge Sorted Lists
# # Question: Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
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
#     # @param two ListNodes
#     # @return a ListNode
#     ___ mergeTwoLists  l1 l2
#         dummy _ ? 0
#         pointer _ ?
#         w___ l1 !_N.. an. l2 !_N..
#             __ ?.v.. < ?.v..
#                 ?.n.. _ ?
#                 l1 _ ?.n..
#             ____
#                 ?.n.. _ ?
#                 l2 _ ?.n..
#             ? _ ?.n..
#         __ l1 __ N..
#             ?.n.. _ ?
#         ____
#             ?.n.. _ l1
#             r_ d__.n..
#
#     ___ printll  node
#         w___ ?
#             print ?.v..
#             n.. _ ?.n..
#
#
# __  -n __ ______
#     ll1 ?.n.. ?.n...n.. _ ? 2 ? 3 ? 5
#     ll2 ?.n.. ?.n...n.. _ ? 4 ? 7 ? 15
#     ? .p..  ? .? ? ?