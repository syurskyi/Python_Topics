"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
"""
__author__ = 'Danyang'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution(object):
    ___ __init__(self):
        self.depth_bottom = {}

    ___ isBalanced(self, root):
        self.fathom(root, 0)
        r.. self._is_balanced(root, 0)

    ___ _is_balanced(self, cur, depth):
        """
        :param depth: depth from root to current node.
        """
        __ n.. cur:
            r.. True

        h1 = h2 = depth
        __ cur.left: h1 = self.depth_bottom[cur.left]
        __ cur.right: h2 = self.depth_bottom[cur.right]

        __ abs(h1 - h2) > 1:
            r.. False

        r.. a..([self._is_balanced(cur.left, depth+1), self._is_balanced(cur.right, depth+1)])

    ___ fathom(self, root, depth):
        __ n.. root:
            r.. depth-1

        ret = max(self.fathom(root.left, depth+1), self.fathom(root.right, depth+1))
        self.depth_bottom[root] = ret
        r.. ret


class SolutionSlow(object):
    ___ isBalanced(self, root):
        """
        pre-order traversal

        :param root: TreeNode
        :return: boolean
        """
        __ n.. root:
            r.. True
        __ abs(self.fathom(root.left, 0)-self.fathom(root.right, 0)) > 1:
            r.. False

        __ self.isBalanced(root.left) a.. self.isBalanced(root.right):
            r.. True
        ____:
            r.. False

    ___ fathom(self, root, depth):
        """
        DFS
        """
        __ n.. root:
            r.. depth-1  # test cases
        r.. max(self.fathom(root.left, depth+1), self.fathom(root.right, depth+1))
