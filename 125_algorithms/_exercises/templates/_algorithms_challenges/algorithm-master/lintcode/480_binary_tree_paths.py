"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    ___ binaryTreePaths(self, root
        """
        :type root: TreeNode
        :rtype: list[str]
        """
        ans =   # list
        __ not root:
            r_ ans

        self.dfs(root, ans,   # list)

        r_ ans

    ___ dfs(self, node, ans, path
        path.append(str(node.val))

        __ not node.left and not node.right:
            ans.append('->'.join(path))
            path.p..
            r_

        __ node.left:
            self.dfs(node.left, ans, path)

        __ node.right:
            self.dfs(node.right, ans, path)

        path.p..
