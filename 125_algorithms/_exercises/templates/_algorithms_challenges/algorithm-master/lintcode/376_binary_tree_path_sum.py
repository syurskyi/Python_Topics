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
    ___ binaryTreePathSum(self, root, target):
        ans    # list
        self.dfs(root, target, ans, [])
        r.. ans

    ___ dfs(self, node, remaining, ans, path):
        __ n.. node:
            r..

        path.a..(node.val)

        remaining -= node.val
        __ remaining __ 0 and n.. node.left and n.. node.right:
            ans.a..(path[:])

        self.dfs(node.left, remaining, ans, path)
        self.dfs(node.right, remaining, ans, path)

        path.pop()
