# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution:
    # @return a ListNode
    ___ addTwoNumbers  l1, l2
        carry = 0
        res = N..
        res_end = N..
        w.... l1 __ n.. N.. a.. l2 __ n.. N..
            temp = l1.val + l2.val + carry
            digit = temp % 10
            carry = temp / 10
            __ res __ N..
                res = ListNode(digit)
                res_end = res
            ____
                res_end.next = ListNode(digit)
                res_end = res_end.next
            l1 = l1.next
            l2 = l2.next
        rem = N..
        __ l1 __ n.. N..
            rem = l1
        ____
            rem = l2
        w.... rem __ n.. N..
            temp = rem.val + carry
            digit = temp % 10
            carry = temp / 10
            __ res __ N..
                res = ListNode(digit)
                res_end = res
            ____
                res_end.next = ListNode(digit)
                res_end = res_end.next
            rem = rem.next
        __ carry __ 1:
            res_end.next = ListNode(1)
            res_end = res_end.next
        r.. res
