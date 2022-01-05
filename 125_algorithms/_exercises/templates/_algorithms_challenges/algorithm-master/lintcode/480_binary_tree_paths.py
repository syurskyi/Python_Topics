"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    ___ binaryTreePaths  root):
        """
        :type root: TreeNode
        :rtype: list[str]
        """
        ans    # list
        __ n.. root:
            r.. ans

        dfs(root, ans, [])

        r.. ans

    ___ dfs  node, ans, path):
        path.a..(s..(node.val))

        __ n.. node.left a.. n.. node.right:
            ans.a..('->'.j..(path))
            path.pop()
            r..

        __ node.left:
            dfs(node.left, ans, path)

        __ node.right:
            dfs(node.right, ans, path)

        path.pop()
