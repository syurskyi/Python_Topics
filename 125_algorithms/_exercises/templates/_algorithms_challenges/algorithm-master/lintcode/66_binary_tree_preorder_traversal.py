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
    @return: Preorder in ArrayList which contains node values.
    """
    ___ preorderTraversal(self, root):
        ans    # list
        __ n.. root:
            r.. ans
        self._traversal(root, ans)
        r.. ans

    ___ _traversal(self, node, res):
        __ n.. node:
            r..

        res.a..(node.val)
        self._traversal(node.left, res)
        self._traversal(node.right, res)
