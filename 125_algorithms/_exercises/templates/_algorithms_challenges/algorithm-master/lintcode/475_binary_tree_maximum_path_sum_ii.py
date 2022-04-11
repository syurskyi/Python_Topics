"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    ___ maxPathSum2  root
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0

        left maxPathSum2(root.left)
        right maxPathSum2(root.right)

        r.. root.val + m..(0, left, right)
