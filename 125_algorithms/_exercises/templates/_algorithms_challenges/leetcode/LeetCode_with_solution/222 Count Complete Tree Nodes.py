"""
Given a complete binary tree, count the number of nodes.

In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""
__author__ = 'Daniel'


class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

    ___ __repr__(self):
        r.. repr(self.val)


class Solution:
    ___ countNodes(self, root):
        """
        O((lg n)^2)
        """
        __ n.. root:
            r.. 0
        h = self.get_height(root)
        h_r = self.get_height(root.right)
        __ h __ h_r+1:
            r.. 2**(h-1)-1+1+self.countNodes(root.right)  # left_tree nodes + root + right_tree nodes
        ____:
            r.. 2**(h-2)-1+1+self.countNodes(root.left)  # right_tree nodes + root + left_tree nodes

    ___ get_height(self, cur):
        h = 0  # depth starting from 0
        w.... cur:
            h += 1
            cur = cur.left

        r.. h


class Solution_TLE:
    ___ __init__(self):
        self.depth = 0  # depth starts from 1
        self.cnt = 0
        self.stopped = False

    ___ countNodes(self, root):
        """

        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0
        self.get_depth(root)
        self.fanthom(root, 1)
        r.. 2**(self.depth-1)-1+self.cnt

    ___ get_depth(self, root):
        self.depth += 1
        __ root.left:
            self.get_depth(root.left)

    ___ fanthom(self, root, depth):
        __ self.stopped:
            r..

        __ n.. root.left a.. n.. root.left:
            __ self.depth __ depth:
                self.cnt += 1
            ____:
                self.stopped = True
            r..

        __ root.left:
            self.fanthom(root.left, depth+1)
        __ root.right:
            self.fanthom(root.right, depth+1)

    ___ countNodes_TLE(self, root):
        """
        Brute Force

        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0

        r.. 1+self.countNodes(root.left)+self.countNodes(root.right)


__ __name__ __ "__main__":
    pass
