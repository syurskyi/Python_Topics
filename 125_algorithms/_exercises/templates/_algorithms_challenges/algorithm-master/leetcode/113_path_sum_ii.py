"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


c_ Solution:
    ___ pathSum  root, target
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        ans    # list

        __ n.. root:
            r.. ans

        dfs(root, target, ans, [])

        r.. ans

    ___ dfs  node, remaining, ans, p..
        __ n.. node:
            r..

        p...a..(node.val)

        __ n.. node.left a.. n.. node.right a.. remaining __ node.val:
            ans.a..(p.. | )
        ____
            dfs(node.left, remaining - node.val, ans, p..)
            dfs(node.right, remaining - node.val, ans, p..)

        p...p.. )
