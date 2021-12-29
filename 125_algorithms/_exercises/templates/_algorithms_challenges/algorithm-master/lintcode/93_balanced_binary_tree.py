"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    ___ isBalanced(self, root):
        return self._divide_conquer(root)[0]

    ___ _divide_conquer(self, node):
        __ not node:
            return True, 0

        is_balanced_left, maxdepth_left = self._divide_conquer(node.left)
        __ not is_balanced_left:
            return False, 0

        is_balanced_right, maxdepth_right = self._divide_conquer(node.right)
        __ not is_balanced_right:
            return False, 0

        return abs(maxdepth_left - maxdepth_right) <= 1, \
            max(maxdepth_left, maxdepth_right) + 1
