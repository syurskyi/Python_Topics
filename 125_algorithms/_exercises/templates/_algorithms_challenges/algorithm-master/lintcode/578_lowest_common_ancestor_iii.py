"""
Notice:
node A or node B may not exist in tree.


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    ___ lowestCommonAncestor3(self, root, a, b):
        """
        :type root: TreeNode
        :type a: TreeNode
        :type b: TreeNode
        :rtype: TreeNode
        """
        __ not root:
            return

        lca, has_a, has_b = self.divide_conquer(root, a, b)

        return lca __ has_a and has_b else None

    ___ divide_conquer(self, node, a, b):
        __ not node:
            return None, False, False

        left, a_in_left, b_in_left = self.divide_conquer(node.left, a, b)
        right, a_in_right, b_in_right = self.divide_conquer(node.right, a, b)

        has_a = a_in_left or a_in_right or node is a
        has_b = b_in_left or b_in_right or node is b

        __ node is a or node is b:
            return node, has_a, has_b
        __ left and right:
            return node, has_a, has_b
        __ left:
            return left, has_a, has_b
        __ right:
            return right, has_a, has_b

        return None, has_a, has_b
