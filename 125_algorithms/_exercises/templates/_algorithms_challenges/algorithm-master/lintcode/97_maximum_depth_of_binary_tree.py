"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    ___ maxDepth(self, root):
        __ n.. root:
            r.. 0

        r.. 1 + max(
            maxDepth(root.left),
            maxDepth(root.right)
        )
