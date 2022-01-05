"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    ___ isBalanced  root):
        r.. _divide_conquer(root)[0]

    ___ _divide_conquer  node):
        __ n.. node:
            r.. T.., 0

        is_balanced_left, maxdepth_left = _divide_conquer(node.left)
        __ n.. is_balanced_left:
            r.. F.., 0

        is_balanced_right, maxdepth_right = _divide_conquer(node.right)
        __ n.. is_balanced_right:
            r.. F.., 0

        r.. abs(maxdepth_left - maxdepth_right) <= 1, \
            m..(maxdepth_left, maxdepth_right) + 1
