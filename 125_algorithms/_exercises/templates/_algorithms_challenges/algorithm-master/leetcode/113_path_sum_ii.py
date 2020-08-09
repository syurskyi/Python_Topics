"""
Definition for a binary tree node.
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    ___ pathSum(self, root, target
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        __ not root:
            r_ ans

        self.dfs(root, target, ans, [])

        r_ ans

    ___ dfs(self, node, remaining, ans, path
        __ not node:
            r_

        path.append(node.val)

        __ not node.left and not node.right and remaining __ node.val:
            ans.append(path[:])
        ____
            self.dfs(node.left, remaining - node.val, ans, path)
            self.dfs(node.right, remaining - node.val, ans, path)

        path.pop()
