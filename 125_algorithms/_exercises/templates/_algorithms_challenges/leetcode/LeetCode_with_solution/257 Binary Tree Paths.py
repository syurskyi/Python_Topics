"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

"""
__author__ = 'Daniel'


class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ___ binaryTreePaths(self, root):
        """

        :type root: TreeNode
        :rtype: list[str]
        """
        __ not root:
            return []

        ret = []
        self.dfs(root, [], ret)
        return ret

    ___ dfs(self, cur, path, ret):
        """
        pre-check
        """
        path.append(cur)
        __ not cur.left and not cur.right:
            ret.append("->".join(map(lambda x: str(x.val), path)))
            return

        __ cur.left:
            self.dfs(cur.left, path, ret)
            path.pop()  # pop the shared path

        __ cur.right:
            self.dfs(cur.right, path, ret)
            path.pop()  # pop the shared path

    ___ dfs_path(self, cur, path, ret):
        __ not cur:
            return

        path.append(cur)
        __ not cur.left and not cur.right:
            ret.append("->".join(map(lambda x: str(x.val), path)))

        self.dfs_path(cur.left, path, ret)
        self.dfs_path(cur.right, path, ret)
        path.pop()
