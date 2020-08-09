"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    min_sum = float('inf')
    node = None

    """
    @param: root: the root of binary tree
    @return: the root of the minimum subtree
    """
    ___ findSubtree(self, root
        self._traversal(root)
        r_ self.node

    ___ _traversal(self, node
        __ not node:
            r_ 0

        left_sum = self._traversal(node.left)
        right_sum = self._traversal(node.right)
        subtree_sum = left_sum + right_sum + node.val

        __ subtree_sum < self.min_sum:
            self.min_sum = subtree_sum
            self.node = node

        r_ subtree_sum
