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
    @return: Inorder in ArrayList which contains node values.
    """
    ___ inorderTraversal  root):
        ans    # list
        __ n.. root:
            r.. ans
        _traversal(root, ans)
        r.. ans

    ___ _traversal  node, res):
        __ n.. node:
            r..

        _traversal(node.left, res)
        res.a..(node.val)
        _traversal(node.right, res)
