"""
Notice:
node A or node B may not exist in tree.


Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    ___ lowestCommonAncestor3(self, root, a, b
        """
        :type root: TreeNode
        :type a: TreeNode
        :type b: TreeNode
        :rtype: TreeNode
        """
        __ not root:
            r_

        lca, has_a, has_b = self.divide_conquer(root, a, b)

        r_ lca __ has_a and has_b else None

    ___ divide_conquer(self, node, a, b
        __ not node:
            r_ None, False, False

        left, a_in_left, b_in_left = self.divide_conquer(node.left, a, b)
        right, a_in_right, b_in_right = self.divide_conquer(node.right, a, b)

        has_a = a_in_left or a_in_right or node is a
        has_b = b_in_left or b_in_right or node is b

        __ node is a or node is b:
            r_ node, has_a, has_b
        __ left and right:
            r_ node, has_a, has_b
        __ left:
            r_ left, has_a, has_b
        __ right:
            r_ right, has_a, has_b

        r_ None, has_a, has_b
