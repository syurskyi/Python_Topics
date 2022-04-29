# # Definition for singly-linked list.
# c_ ListNode o..
#     ___ -  x
#         val  ?
#         next  N..
#
#
# c_ Solution o..
#     # def addTwoNumbers(self, l1, l2):
#     #     """
#     #     :type l1: ListNode
#     #     :type l2: ListNode
#     #     :rtype: ListNode
#     #     """
#     #     last = 0
#     #     head = prev = None
#     #     while True:
#     #         if l2 is None and l1 is None and last == 0:
#     #             break
#     #         val = last
#     #         if l2 is not None:
#     #             val += l2.val
#     #             l2 = l2.next
#     #         if l1 is not None:
#     #             val += l1.val
#     #             l1 = l1.next
#     #         if val >= 10:
#     #             val = val % 10
#     #             last = 1
#     #         else:
#     #             last = 0
#     #         current = ListNode(val)
#     #         if prev is None:
#     #             head = current
#     #         else:
#     #             prev.next = current
#     #         prev = current
#     #     return head
#
#     ___ addTwoNumbers  l1 l2
#         carry  0
#         # dummy head
#         head _ curr _ ? 0
#         w.. l1 \\ l2
#             val  carry
#             __ ?
#                 ? +_ ?.v..
#                 ?  ?.n..
#             __ ?
#                 v.. +_ ?.v..
#                 ?  ?.n..
#             curr.n..  ? ? % 10
#             curr  ?.n..
#             carry  v.. / 10
#         __ ? > 0
#             ?.n..  ? ?
#         r_ ?.n..
