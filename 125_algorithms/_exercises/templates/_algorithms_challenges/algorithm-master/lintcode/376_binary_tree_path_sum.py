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
    ___ binaryTreePathSum  root, target):
        ans    # list
        dfs(root, target, ans, [])
        r.. ans

    ___ dfs  node, remaining, ans, path):
        __ n.. node:
            r..

        path.a..(node.val)

        remaining -= node.val
        __ remaining __ 0 a.. n.. node.left a.. n.. node.right:
            ans.a..(path | )

        dfs(node.left, remaining, ans, path)
        dfs(node.right, remaining, ans, path)

        path.pop()
