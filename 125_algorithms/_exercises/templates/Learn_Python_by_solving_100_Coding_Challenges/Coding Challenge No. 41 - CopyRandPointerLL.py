# # Copy linked list with random pointer
# # Question: A linked list is given such that each node contains an additional random pointer which could point to any
# # node in the list or null.
# # Return a deep copy of the list.
# # Solutions:
#
#
# c_ RandomListNode
#     ___  -  x
#         val _ x
#         next _ N..
#         ra__ _ N..
#
#
# c_ Solution
#     # @param ll, a RandomListNode
#     # @return a RandomListNode
#
#     ___ copyRandomList  ll
#         # copy and combine copied list with original list
#         current _ ?
#         w___ ?
#             copied _ R.. ?.v..
#             copied.n.. _ ?.n..
#             ?.n.. _ copied
#             ? _ copied.n..
#
#         # update random node in copied list
#         current _ ll
#         w___ ?
#             __ ?.ra__
#                 ?.n...ra__ _ ?.ra__.n..
#             ? _ ?.n...n..
#
#         # split copied list from combined one
#         dummy _ R.. 0
#         copied_current, ? _ ? ?
#         w___ ?
#             ?.n.. _ ?.n..
#             ?.n.. _ ?.n...n..
#             ? ? _ ?.n.. ?.n..
#         r_ ?.n..
#
#
# __  -n __ _____
#     ll, ll.n.. _ ? 1, ? 2,
#     ll.ra__ _ ll.n..
#     result _ ? .? ?
#     print ?.v..
#     print ?.n...v..
#     print ?.ra__.v..