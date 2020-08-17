"""
Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    find path count
    """
    ___ pathSum(self, root, target
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        __ not root:
            r_ 0

        r_ su.((
            self.count_valid_path(root, target),
            self.pathSum(root.left, target),
            self.pathSum(root.right, target),
        ))

    ___ count_valid_path(self, node, remaining
        __ not node:
            r_ 0

        r_ su.((
            int(node.val __ remaining),
            self.count_valid_path(node.left, remaining - node.val),
            self.count_valid_path(node.right, remaining - node.val),
        ))


class Solution:
    """
    print path
    """
    ___ pathSum(self, root, target
        """
        :type root: TreeNode
        :type target: int
        :rtype: list[list[int]]
        """
        ans = []

        __ not root:
            r_ ans

        self.dfs(root, target, ans, [])

        r_ ans

    ___ dfs(self, node, target, ans, path
        __ not node:
            r_

        path.append(node.val)

        remaining = target
        ___ i in range(le.(path) - 1, -1, -1
            remaining -= path[i]

            __ remaining __ 0:
                ans.append(path[i:])

        self.dfs(node.left, target, ans, path)
        self.dfs(node.right, target, ans, path)
        path.p..
