"""
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you
implement both?
"""

# Definition for singly-linked list.
c_ ListNode(o..
    ___ - , x
        val x
        next N..


c_ Solution(o..
    ___ reverseList  head
        """
        :type head: ListNode
        :rtype: ListNode

        Recursive (Time Limit Exceeded)
        """
        __ head __ N..
            r.. N..
        ____
            rev_rest reverseList(head.next)
            current rev_rest
            __ current __ N..
                r.. head
            w.... current a.. current.next __ n.. N..
                current current.next
            current.next head
            head.next N..
            r.. rev_rest


n1 ListNode(1)
n2 ListNode(2)
n3 ListNode(3)
n1.next n2
n2.next n3
s Solution()
r1 s.reverseList(n1)
print r1.val
print r1.next.val
print r1.next.next.val
