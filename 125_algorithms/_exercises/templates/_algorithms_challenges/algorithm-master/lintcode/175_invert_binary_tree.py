"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    ___ invertBinaryTree  root
        divide_conquer(root)

    ___ divide_conquer  node
        __ n.. node:
            r..

        divide_conquer(node.left)
        divide_conquer(node.right)

        node.left, node.right node.right, node.left
