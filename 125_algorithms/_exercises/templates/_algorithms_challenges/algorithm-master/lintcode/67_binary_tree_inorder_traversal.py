"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    ___ inorderTraversal(self, root
        ans = []
        __ not root:
            r_ ans
        self._traversal(root, ans)
        r_ ans

    ___ _traversal(self, node, res
        __ not node:
            r_

        self._traversal(node.left, res)
        res.append(node.val)
        self._traversal(node.right, res)
