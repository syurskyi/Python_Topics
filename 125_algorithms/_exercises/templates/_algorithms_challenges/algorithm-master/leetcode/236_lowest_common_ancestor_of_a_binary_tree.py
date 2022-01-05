# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution(o..):
    ___ lowestCommonAncestor  root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        __ n.. root o. root __ p o. root __ q:
            r.. root

        left = lowestCommonAncestor(root.left, p, q)
        right = lowestCommonAncestor(root.right, p, q)

        __ left a.. right:
            r.. root
        __ left:
            r.. left
        __ right:
            r.. right
