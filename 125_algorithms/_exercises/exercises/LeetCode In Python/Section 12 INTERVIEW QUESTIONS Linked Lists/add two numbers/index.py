# # Definition for singly-linked list.
# # class ListNode:
# #     ___ __init__(self, x
# #         self.val = x
# #         self.next = None
#
# c_ Solution
#     ___ addTwoNumbers l1 LN.. l2 LN..  LN..
#         ans _ LN.. N..
#         pointer _ ?
#
#         carry _ 0
#         su. _ 0
#
#         w___ l1!N.. o.. l2!N..
#             su. _ c..
#             __ ?!N..
#                 su.+_?.v..
#                 l1 _ ?.n..
#             __ ?!N..
#                 su.+_?.v..
#                 l2 _ ?.v..
#
#             carry _ in.(su./10)
#             p__.n..  _ LN.. su.%10
#
#             p.. _ p__.n..
#
#         __ c.. > 0
#             p__.n.. _ LN.. c..
#
#         r_ assert.n..