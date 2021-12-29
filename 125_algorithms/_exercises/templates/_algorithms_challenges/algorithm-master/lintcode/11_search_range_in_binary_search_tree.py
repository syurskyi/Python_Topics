"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    ___ searchRange(self, root, a, b):
        """
        :type root: TreeNode
        :type a: int
        :type b: int
        :rtype: list[int]
        """
        ans = []

        __ not root:
            return ans

        self.dfs(root, a, b, ans)

        return ans

    ___ dfs(self, node, a, b, ans):
        __ not node:
            return

        self.dfs(node.left, a, b, ans)

        __ a <= node.val <= b:
            ans.append(node.val)

        self.dfs(node.right, a, b, ans)
