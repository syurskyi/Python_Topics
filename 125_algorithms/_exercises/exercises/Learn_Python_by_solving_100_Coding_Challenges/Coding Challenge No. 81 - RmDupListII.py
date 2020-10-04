# # Remove Duplicates from Sorted List II
# # Question: Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# # For example:
# # Given 1->2->3->3->4->4->5, return 1->2->5.
# # Given 1->1->1->2->3, return 2->3.
# # Solutions:
#
# c_ ListNode
#     ___  -  x
#         val _ ?
#         next _ N..
#
#
# c_ Solution
#     # @param head, a ListNode
#     # @return a ListNode
#     ___ deleteDuplicates  head
#         __ head __ N..
#             r_ N..
#         dummy _ ? 10**10
#         ?.n.. h.. _ ? ? # add a dummy node
#         pprev prev curr dupFlag _ h.. h__.n.. h__.n...n.. F..
#         w___ T..
#             __ dupFlag __ T..
#                 __ c.. __ N..
#                     p__.n.. _ N..
#                     b..
#                 __ p__.v.. !_ c__.v..
#                     p__.n.. p.. d.. _ c.. c.. F..
#             ____
#                 __ c.. __ N..
#                     b..
#                 __ p__.v.. __ c__.v..
#                     d.. _ T..
#                 ____
#                     p__ p.. _ ?.n.. ?.n..
#             c.. _ ?.n..
#         r_ ?.n..
#
#     ___ printll  node
#         w___ ?
#             print ?.v..
#             n.. _ ?.n..
#
#
# __  -n __ ______
#     ll1 ?.n.. ?.n...n.. _ ? 2 ? 2 ? 5
#     ? .p..  ? .? ?