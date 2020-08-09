# Definition for singly-linked list.
# class ListNode:
#     ___ __init__(self, x
#         self.val = x
#         self.next = None


class Solution:
    ___ mergeTwoLists(self, a, b
        """
        :type a: ListNode
        :type b: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(-1)

        w___ a and b:
            __ a.val < b.val:
                tail.next = ListNode(a.val)
                a = a.next
            ____
                tail.next = ListNode(b.val)
                b = b.next
            tail = tail.next

        w___ a:
            tail.next = ListNode(a.val)
            a = a.next
            tail = tail.next

        w___ b:
            tail.next = ListNode(b.val)
            b = b.next
            tail = tail.next

        r_ dummy.next
