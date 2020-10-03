# # Linked List Cycle II
# # Question: Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# # Solutions:
#
#
#
# c_ ListNode
#     ___  -  val next_None
#         ? _ ?
#         ? _ ?
#
#
# c_ Solution
#     """
#     @param head: The first node of the linked list.
#     @return: the node where the cycle begins. If there is no cycle, return null
#     """
#
#     ___ detectCycle head
#         __ ? __ N.. o. ?.n.. __ N..
#             r_ N..
#         slow _ fast _ ?
#         w___ f.. an. f__.n..
#             s.. _ s__.n..
#             f.. _ f__.n...n..
#             __ f.. __ s..
#                 b..
#         __ s.. __ f...
#             s.. _ ?
#             w___ ? !_ ?
#                 s.. _ ?.n..
#                 f.. _ ?.n..
#             r_ ?
#         r_ N..
#
#
# __  -n __ ______
#     ll, ?.n.., ?.n...n.. _ ? 2 ? 4 ? 3
#     ?.n...n...n.. _ ?.n..
#     print ? .? ?.v..