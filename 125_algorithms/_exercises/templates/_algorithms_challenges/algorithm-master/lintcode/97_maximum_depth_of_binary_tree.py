"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    ___ maxDepth(self, root
        __ not root:
            r_ 0

        r_ 1 + ma.(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )
