# # Linked List Cycle
# # Question: Given a linked list, determine if it has a cycle in it
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
#     # @return a boolean
#     ___ hasCycle  head
#         __ ? __ N.. o. ?.n.. __ N..
#             r_ F..
#         slow _ fast _ ?
#         w___ f.. an. ?.n..
#             s.. _ ?.n..
#             f.. _ ?.n__.n..
#             __ ? __ f..
#                 r_ T..
#         r_ F..
#
# __  -n __ ______
#     ll ?.n.. ?.n__.n.. _ ? 2 ? 4 ? 3
#     ?.n__.n__.n.. _ ?.n..
#     print  ? .? ?