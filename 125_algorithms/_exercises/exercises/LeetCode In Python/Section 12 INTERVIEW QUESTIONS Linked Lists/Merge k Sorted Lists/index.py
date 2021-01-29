# # Definition for singly-linked list.
# # class ListNode:
# #     ___ __init__(self, x
# #         self.val = x
# #         self.next = None
#
#
# c_ Solution
#
#     ___ mergeTwoLists l1 l2
#         cur _ LN.. 0
#         ans _ cur
#
#         w___ ? a.. ?
#             __ ?.v.. > ?.v..
#                 c__.n.. _ ?
#                 ? _ ?.n..
#
#             ____
#                 c__.n.. _ ?
#                 ? _ ?.n..
#             cur _ c__.n..
#
#         w___ ?
#             c__.n.. _ ?
#             ? _ ?.n..
#             cur _ c__.n..
#         w___ ?
#             c__.n.. _ ?
#             ? _ ?.n..
#             c__ _ c__.n..
#         r_ assert.n..
#
#     ___ mergeKLists lists L.. LN..  LN..
#         __ le. ? __ 0
#             r_ N..
#
#         i _ 0
#         last _ le. ? -1
#         j _ ?
#
#         w___ ? !_ 0
#             i _ 0
#             j _ l..
#
#             w___ ? > ?
#                 l.. ? _ .m.. l.. ? l.. ?
#                 ? +_ 1
#                 ? -_ 1
#                 l.. _ ?
#
#         r_ l.. 0
