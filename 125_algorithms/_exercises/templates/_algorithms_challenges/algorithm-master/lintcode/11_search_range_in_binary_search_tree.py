"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    ___ searchRange  root, a, b):
        """
        :type root: TreeNode
        :type a: int
        :type b: int
        :rtype: list[int]
        """
        ans    # list

        __ n.. root:
            r.. ans

        dfs(root, a, b, ans)

        r.. ans

    ___ dfs  node, a, b, ans):
        __ n.. node:
            r..

        dfs(node.left, a, b, ans)

        __ a <= node.val <= b:
            ans.a..(node.val)

        dfs(node.right, a, b, ans)
