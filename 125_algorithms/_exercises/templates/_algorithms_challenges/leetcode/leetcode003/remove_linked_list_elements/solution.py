"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution(o..
    ___ removeElements  head, val
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        __ head __ N..
            r.. N..
        current head
        last N..
        w.... current __ n.. N..
            __ current.val __ val:
                __ last __ n.. N..
                    # Remove `current` node and `last` node is not changed
                    last.next current.next
                ____
                    # `current` is the head node
                    # Remove the head node and `last` node is still None
                    head current.next
                    last N..
            ____
                last current
            current current.next
        r.. head
