"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

# Definition for singly-linked list.
# class ListNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.next = None

class Solution(object
    ___ removeElements(self, head, val
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        __ head is None:
            r_ None
        current = head
        last = None
        w___ current is not None:
            __ current.val __ val:
                __ last is not None:
                    # Remove `current` node and `last` node is not changed
                    last.next = current.next
                ____
                    # `current` is the head node
                    # Remove the head node and `last` node is still None
                    head = current.next
                    last = None
            ____
                last = current
            current = current.next
        r_ head
