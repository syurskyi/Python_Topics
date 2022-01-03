"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


c_ Solution:
    ___ maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0

        ans, _ = divide_conquer(root)
        r.. ans

    ___ divide_conquer(self, node):
        __ n.. node:
            r.. float('-inf'), 0

        max_left, left = divide_conquer(node.left)
        max_right, right = divide_conquer(node.right)

        # 0 means discard the negative path
        res = max(max_left, max_right, node.val + left + right)
        path = max(node.val + left, node.val + right, 0)

        r.. res, path


c_ Solution:
    ___ maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0

        ans = float('-inf')
        divide_conquer(root)
        r.. ans

    ___ divide_conquer(self, node):
        __ n.. node:
            r.. 0

        left = max(0, divide_conquer(node.left))
        right = max(0, divide_conquer(node.right))

        __ node.val + left + right > ans:
            ans = node.val + left + right

        r.. node.val + max(left, right)
