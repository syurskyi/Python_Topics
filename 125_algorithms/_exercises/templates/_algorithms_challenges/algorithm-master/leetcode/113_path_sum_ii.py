"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


c_ Solution:
    ___ pathSum(self, root, target):
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

    ___ dfs(self, node, remaining, ans, path):
        __ n.. node:
            r..

        path.a..(node.val)

        __ n.. node.left a.. n.. node.right a.. remaining __ node.val:
            ans.a..(path | )
        ____:
            dfs(node.left, remaining - node.val, ans, path)
            dfs(node.right, remaining - node.val, ans, path)

        path.pop()
