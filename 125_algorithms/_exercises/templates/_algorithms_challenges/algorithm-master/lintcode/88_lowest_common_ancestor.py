"""
Notice:
Assume two nodes are exist in tree.


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    ___ lowestCommonAncestor  root, a, b
        """
        :type root: TreeNode
        :type a: TreeNode
        :type b: TreeNode
        :rtype: TreeNode
        """
        __ n.. root o. root __ a o. root __ b:
            r.. root

        left lowestCommonAncestor(root.left, a, b)
        right lowestCommonAncestor(root.right, a, b)

        __ left a.. right:
            r.. root
        __ left:
            r.. left
        __ right:
            r.. right
