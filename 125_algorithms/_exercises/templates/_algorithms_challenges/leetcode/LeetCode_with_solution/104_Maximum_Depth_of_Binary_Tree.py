# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution:
    ___ maxDepth  root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ root is N..:
            r_ 0
        ld = maxDepth(root.left)
        rd = maxDepth(root.right)
        r_ 1 + max(ld, rd)
