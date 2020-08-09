# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    ___ splitBST(self, root, target
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[TreeNode]
        """
        __ not root:
            r_ None, None

        __ root.val > target:
            left, right = self.splitBST(root.left, target)
            root.left = right
            r_ left, root
        ____
            left, right = self.splitBST(root.right, target)
            root.right = left
            r_ root, right
