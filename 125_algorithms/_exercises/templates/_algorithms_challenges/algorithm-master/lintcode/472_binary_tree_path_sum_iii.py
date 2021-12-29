"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    ___ binaryTreePathSum3(self, root, target):
        """
        1. using `dfs` to visit every node in that tree
        2. once enter a node, start to find the path based on it
           to parent, left child, and right child.
        """
        ans    # list
        self.dfs(root, target, ans)
        r.. ans

    ___ dfs(self, node, target, ans):
        __ n.. node:
            r..

        self.find_path(node, node, target, ans, [])

        self.dfs(node.left, target, ans)
        self.dfs(node.right, target, ans)

    ___ find_path(self, node, start, remaining, ans, path):
        path.a..(node.val)

        remaining -= node.val
        __ remaining __ 0:
            ans.a..(path[:])

        __ node.parent and node.parent __ n.. start:
            self.find_path(node.parent, node, remaining, ans, path)
        __ node.left and node.left __ n.. start:
            self.find_path(node.left, node, remaining, ans, path)
        __ node.right and node.right __ n.. start:
            self.find_path(node.right, node, remaining, ans, path)

        path.pop()
