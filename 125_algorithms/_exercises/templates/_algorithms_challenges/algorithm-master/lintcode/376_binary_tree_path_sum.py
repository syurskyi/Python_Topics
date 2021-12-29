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
        ans = []
        self.dfs(root, target, ans, [])
        return ans

    ___ dfs(self, node, remaining, ans, path):
        __ not node:
            return

        path.append(node.val)

        remaining -= node.val
        __ remaining == 0 and not node.left and not node.right:
            ans.append(path[:])

        self.dfs(node.left, remaining, ans, path)
        self.dfs(node.right, remaining, ans, path)

        path.pop()
