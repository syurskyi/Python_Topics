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
        ans = []
        __ not root:
            return ans
        self._traversal(root, ans)
        return ans

    ___ _traversal(self, node, res):
        __ not node:
            return

        self._traversal(node.left, res)
        res.append(node.val)
        self._traversal(node.right, res)
