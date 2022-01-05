"""
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c_ Solution:
    # @param head, a list node
    # @return a tree node
    ___ sortedListToBST  head):
        __ head __ N..
            r.. N..
        ____:
            # Get the middle node
            slow = head
            fast = head
            prev = N..  # Previous node to slow (mid)
            w.... fast.next __ n.. N.. a.. fast.next.next __ n.. N..
                prev = slow
                fast = fast.next.next
                slow = slow.next
            __ head __ slow:
                head = N..
            __ prev __ n.. N..
                prev.next = N..
            root = TreeNode(slow.val)
            left = sortedListToBST(head)
            right = sortedListToBST(slow.next)
            root.left = left
            root.right = right
            r.. root
