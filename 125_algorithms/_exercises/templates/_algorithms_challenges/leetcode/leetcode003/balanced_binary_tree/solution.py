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

class Solution(object):
    ___ isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ root __ N..
            r.. True
        ____:
            __ self.isBalanced(root.left) and self.isBalanced(root.right):
                r.. abs(self.depth(root.left) - self.depth(root.right)) <= 1
            ____:
                r.. False

    ___ depth(self, root):
        __ root __ N..
            r.. -1
        ____:
            r.. max(self.depth(root.left), self.depth(root.right)) + 1
