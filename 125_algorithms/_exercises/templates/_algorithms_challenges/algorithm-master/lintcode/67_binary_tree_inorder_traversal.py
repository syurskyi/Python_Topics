"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    ___ inorderTraversal(self, root):
        ans    # list
        __ n.. root:
            r.. ans
        self._traversal(root, ans)
        r.. ans

    ___ _traversal(self, node, res):
        __ n.. node:
            r..

        self._traversal(node.left, res)
        res.a..(node.val)
        self._traversal(node.right, res)
