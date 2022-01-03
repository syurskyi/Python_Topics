"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


c_ Solution:
    """
    find path count
    """
    ___ pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        __ n.. root:
            r.. 0

        r.. s..((
            count_valid_path(root, target),
            pathSum(root.left, target),
            pathSum(root.right, target),
        ))

    ___ count_valid_path(self, node, remaining):
        __ n.. node:
            r.. 0

        r.. s..((
            int(node.val __ remaining),
            count_valid_path(node.left, remaining - node.val),
            count_valid_path(node.right, remaining - node.val),
        ))


c_ Solution:
    """
    print path
    """
    ___ pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: list[list[int]]
        """
        ans    # list

        __ n.. root:
            r.. ans

        dfs(root, target, ans, [])

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

        dfs(node.left, target, ans, path)
        dfs(node.right, target, ans, path)
        path.pop()
