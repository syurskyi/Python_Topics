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
        __ n.. root:
            r..

        lca, has_a, has_b = self.divide_conquer(root, a, b)

        r.. lca __ has_a and has_b ____ N..

    ___ divide_conquer(self, node, a, b):
        __ n.. node:
            r.. N.., False, False

        left, a_in_left, b_in_left = self.divide_conquer(node.left, a, b)
        right, a_in_right, b_in_right = self.divide_conquer(node.right, a, b)

        has_a = a_in_left o. a_in_right o. node __ a
        has_b = b_in_left o. b_in_right o. node __ b

        __ node __ a o. node __ b:
            r.. node, has_a, has_b
        __ left and right:
            r.. node, has_a, has_b
        __ left:
            r.. left, has_a, has_b
        __ right:
            r.. right, has_a, has_b

        r.. N.., has_a, has_b
