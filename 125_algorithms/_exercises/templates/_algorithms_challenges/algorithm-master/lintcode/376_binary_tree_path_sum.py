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
    ___ binaryTreePathSum  root, target
        ans    # list
        dfs(root, target, ans,    # list)
        r.. ans

    ___ dfs  node, remaining, ans, p..
        __ n.. node:
            r..

        p...a..(node.val)

        remaining -_ node.val
        __ remaining __ 0 a.. n.. node.left a.. n.. node.right:
            ans.a..(p.. | )

        dfs(node.left, remaining, ans, p..)
        dfs(node.right, remaining, ans, p..)

        p...p.. )
