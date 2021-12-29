"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    ___ binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: list[str]
        """
        ans    # list
        __ n.. root:
            r.. ans

        self.dfs(root, ans, [])

        r.. ans

    ___ dfs(self, node, ans, path):
        path.a..(s..(node.val))

        __ n.. node.left a.. n.. node.right:
            ans.a..('->'.join(path))
            path.pop()
            r..

        __ node.left:
            self.dfs(node.left, ans, path)

        __ node.right:
            self.dfs(node.right, ans, path)

        path.pop()
