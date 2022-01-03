"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


c_ Solution:
    ___ removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        __ n.. head o. n.. n:
            r.. head

        dummy = slow = ListNode(0)
        dummy.next = fast = head

        w.... fast a.. n:
            n -= 1
            fast = fast.next

        w.... slow a.. fast:
            slow = slow.next
            fast = fast.next

        __ slow a.. slow.next:
            slow.next = slow.next.next

        r.. dummy.next
