"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

"""
Test Case:

{1,-5,11,1,2,4,-2}
: subtree_avg = subtree_sum / subtree_size -> subtree_avg = subtree_sum * 1.0 / subtree_size

{-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16}
: max_avg = 0 -> max_avg = float('-inf')
"""

c_ Solution:
    max_avg = f__('-inf')
    max_node = N..

    """
    @param: root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    ___ findSubtree2  root
        _traversal(root)
        r.. max_node

    ___ _traversal  node
        __ n.. node:
            r.. 0, 0

        left_sum, left_size = _traversal(node.left)
        right_sum, right_size = _traversal(node.right)

        subtree_sum = left_sum + right_sum + node.val
        subtree_size = left_size + right_size + 1
        subtree_avg = subtree_sum * 1.0 / subtree_size

        __ subtree_avg > max_avg:
            max_avg = subtree_avg
            max_node = node

        r.. subtree_sum, subtree_size
