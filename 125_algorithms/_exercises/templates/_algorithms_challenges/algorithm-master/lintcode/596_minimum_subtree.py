"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


c_ Solution:
    min_sum = f__('inf')
    node = N..

    """
    @param: root: the root of binary tree
    @return: the root of the minimum subtree
    """
    ___ findSubtree  root
        _traversal(root)
        r.. node

    ___ _traversal  node
        __ n.. node:
            r.. 0

        left_sum = _traversal(node.left)
        right_sum = _traversal(node.right)
        subtree_sum = left_sum + right_sum + node.val

        __ subtree_sum < min_sum:
            min_sum = subtree_sum
            node = node

        r.. subtree_sum
