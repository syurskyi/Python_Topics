"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution(o..
    ___ isBalanced  root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ root __ N..
            r.. T..
        ____:
            __ isBalanced(root.left) a.. isBalanced(root.right
                r.. abs(depth(root.left) - depth(root.right <= 1
            ____:
                r.. F..

    ___ depth  root
        __ root __ N..
            r.. -1
        ____:
            r.. m..(depth(root.left), depth(root.right + 1
