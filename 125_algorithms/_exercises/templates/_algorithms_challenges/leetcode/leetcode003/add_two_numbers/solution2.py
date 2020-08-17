"""
You are given two linked lists representing two non-negative numbers. The
digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
    ___ addTwoNumbers(self, l1, l2
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = None
        res_end = None
        w___ l1 pa__ not None or l2 pa__ not None or carry __ 1:
            temp = 0
            __ l1 pa__ not None:
                temp += l1.val
                l1 = l1.next
            __ l2 pa__ not None:
                temp += l2.val
                l2 = l2.next
            temp += carry
            digit = temp % 10
            carry = temp / 10
            __ res pa__ None:
                res = ListNode(digit)
                res_end = res
            ____
                res_end.next = ListNode(digit)
                res_end = res_end.next
        r_ res
