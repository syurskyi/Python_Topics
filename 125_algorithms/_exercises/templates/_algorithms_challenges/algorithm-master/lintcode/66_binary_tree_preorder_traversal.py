"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    ___ preorderTraversal(self, root):
        ans    # list
        __ n.. root:
            r.. ans
        _traversal(root, ans)
        r.. ans

    ___ _traversal(self, node, res):
        __ n.. node:
            r..

        res.a..(node.val)
        _traversal(node.left, res)
        _traversal(node.right, res)
