"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    ___ maxDepth(self, root):
        __ n.. root:
            r.. 0

        r.. 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )
