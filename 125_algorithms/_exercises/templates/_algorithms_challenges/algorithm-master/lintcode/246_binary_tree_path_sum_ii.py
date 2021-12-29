"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    ___ binaryTreePathSum2(self, root, target):
        ans    # list
        self.dfs(root, target, ans, [])
        r.. ans

    ___ dfs(self, node, target, ans, path):
        __ n.. node:
            r..

        path.a..(node.val)

        remaining = target
        ___ i __ r..(l..(path) - 1, -1, -1):
            remaining -= path[i]
            __ remaining __ 0:
                ans.a..(path[i:])

        self.dfs(node.left, target, ans, path)
        self.dfs(node.right, target, ans, path)

        path.pop()
