"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    find path count
    """
    ___ pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        __ not root:
            return 0

        return sum((
            self.count_valid_path(root, target),
            self.pathSum(root.left, target),
            self.pathSum(root.right, target),
        ))

    ___ count_valid_path(self, node, remaining):
        __ not node:
            return 0

        return sum((
            int(node.val == remaining),
            self.count_valid_path(node.left, remaining - node.val),
            self.count_valid_path(node.right, remaining - node.val),
        ))


class Solution:
    """
    print path
    """
    ___ pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: list[list[int]]
        """
        ans = []

        __ not root:
            return ans

        self.dfs(root, target, ans, [])

        return ans

    ___ dfs(self, node, target, ans, path):
        __ not node:
            return

        path.append(node.val)

        remaining = target
        for i in range(len(path) - 1, -1, -1):
            remaining -= path[i]

            __ remaining == 0:
                ans.append(path[i:])

        self.dfs(node.left, target, ans, path)
        self.dfs(node.right, target, ans, path)
        path.pop()
