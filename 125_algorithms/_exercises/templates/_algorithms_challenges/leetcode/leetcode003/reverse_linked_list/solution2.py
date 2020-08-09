"""
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you
implement both?
"""

# Definition for singly-linked list.
class ListNode(object
    ___ __init__(self, x
        self.val = x
        self.next = None


class Solution(object
    ___ reverseList(self, head
        """
        :type head: ListNode
        :rtype: ListNode

        Recursive (Time Limit Exceeded)
        """
        __ head is None:
            r_ None
        ____
            rev_rest = self.reverseList(head.next)
            current = rev_rest
            __ current is None:
                r_ head
            w___ current and current.next is not None:
                current = current.next
            current.next = head
            head.next = None
            r_ rev_rest


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
s = Solution()
r1 = s.reverseList(n1)
print r1.val
print r1.next.val
print r1.next.next.val
