"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    ___ binaryTreePathSum2  root, target):
        ans    # list
        dfs(root, target, ans, [])
        r.. ans

    ___ dfs  node, target, ans, path):
        __ n.. node:
            r..

        path.a..(node.val)

        remaining = target
        ___ i __ r..(l..(path) - 1, -1, -1):
            remaining -= path[i]
            __ remaining __ 0:
                ans.a..(path[i:])

        dfs(node.left, target, ans, path)
        dfs(node.right, target, ans, path)

        path.pop()
