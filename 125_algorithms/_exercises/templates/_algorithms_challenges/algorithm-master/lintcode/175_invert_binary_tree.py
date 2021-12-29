"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    ___ invertBinaryTree(self, root):
        self.divide_conquer(root)

    ___ divide_conquer(self, node):
        __ n.. node:
            r..

        self.divide_conquer(node.left)
        self.divide_conquer(node.right)

        node.left, node.right = node.right, node.left
