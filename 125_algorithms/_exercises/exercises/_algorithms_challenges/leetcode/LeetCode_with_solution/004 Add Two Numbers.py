# """
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each
# of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# """
#
# __author__ = 'Danyang'
#
#
# c_ ListNode
#     ___ -  x
#         val ?
#         next  N..
#
#     ___  -r
#         # for debugging
#         r.. r.. ?
#
#
# c_ Solution
#     ___ addTwoNumbers  l1 l2
#         """
#         Algorithm: Two pointers & math
#         Two pointers for l1 and l2 respectively
#         Math - carry for addition, in the form of new node
#
#         :param l1: linked list head node
#         :param l2: linked list head node
#         :return: ListNode
#         """
#         result_head  ? 0
#
#         cur1 ?
#         cur2 ?
#         cur  ?
#         w.... __1 o. __2
#             ?.v..  ?.v..+a.. ? ?
#             __ ?.v.. < 10
#                 __ __1 a.. __1.n.. o. __2 a.. __2.n..  # next node
#                     ?.n.. ? 0
#             ____
#                 ?.v.. -_ 10
#                 ?.n..  ? 1
#
#             __ __1
#                 __1  __1.n..
#             __ __2
#                 __2  __2.n..
#             cur  ?.n..
#
#         r.. ?
#
#     ___ addNode  node1 node2
#         """
#         Handles None situation
#
#         :param node1: ListNode
#         :param node2: ListNode
#         :return: integer, summation
#         """
#         __ n.. ? a.. n.. ?
#             r.. E.. "two nodes are None"
#         __ n.. ?
#             r.. ?.v..
#         __ n.. ?
#             r.. ?.v..
#         r.. __1.v..+__2.v..
#
#
# __ _______ __ _______
#     l1s ? 1
#     l2s  ? 9 ? 9
#     ___ i __ r.. l.. ? - 1
#         ? ?.n..  ? ? + 1
#     ___ i __ r.. l..? - 1
#         ? ?.n.. _ ? ?+1
#     ?.a.. ? 0 ? 0
