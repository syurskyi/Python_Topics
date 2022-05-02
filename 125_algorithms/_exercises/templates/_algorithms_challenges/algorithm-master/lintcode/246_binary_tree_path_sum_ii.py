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
    ___ binaryTreePathSum2  root, target
        ans    # list
        dfs(root, target, ans,    # list)
        r.. ans

    ___ dfs  node, target, ans, p..
        __ n.. node:
            r..

        p...a..(node.val)

        remaining target
        ___ i __ r..(l..(p..) - 1, -1, -1
            remaining -_ p..[i]
            __ remaining __ 0:
                ans.a..(p..[i:])

        dfs(node.left, target, ans, p..)
        dfs(node.right, target, ans, p..)

        p...p.. )
