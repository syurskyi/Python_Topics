"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    ___ removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        __ not head or not n:
            return head

        dummy = slow = ListNode(0)
        dummy.next = fast = head

        while fast and n:
            n -= 1
            fast = fast.next

        while slow and fast:
            slow = slow.next
            fast = fast.next

        __ slow and slow.next:
            slow.next = slow.next.next

        return dummy.next
