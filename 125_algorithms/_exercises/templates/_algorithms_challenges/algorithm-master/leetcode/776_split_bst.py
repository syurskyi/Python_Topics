# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    ___ splitBST(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[TreeNode]
        """
        __ not root:
            return None, None

        __ root.val > target:
            left, right = self.splitBST(root.left, target)
            root.left = right
            return left, root
        else:
            left, right = self.splitBST(root.right, target)
            root.right = left
            return root, right
