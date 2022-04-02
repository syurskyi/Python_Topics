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
            __ height(root) != -1:
                r.. T..
            ____:
                r.. F..

    ___ height  root
        # Return -1 if not balanced
        __ root __ N..
            r.. 0
        ____:
            left_height = height(root.left)
            right_height = height(root.right)
            __ left_height __ -1 o. right_height __ -1:
                r.. -1
            ____:
                __ abs(left_height - right_height) <= 1:
                    r.. m..(left_height, right_height) + 1
                ____:
                    r.. -1
