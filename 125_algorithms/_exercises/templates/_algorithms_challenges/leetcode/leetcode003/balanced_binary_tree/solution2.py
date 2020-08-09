"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a binary tree node.
# class TreeNode(object
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object
    ___ isBalanced(self, root
        """
        :type root: TreeNode
        :rtype: bool
        """
        __ root is None:
            r_ True
        ____
            __ self.height(root) != -1:
                r_ True
            ____
                r_ False

    ___ height(self, root
        # Return -1 if not balanced
        __ root is None:
            r_ 0
        ____
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            __ left_height __ -1 or right_height __ -1:
                r_ -1
            ____
                __ abs(left_height - right_height) <= 1:
                    r_ max(left_height, right_height) + 1
                ____
                    r_ -1
