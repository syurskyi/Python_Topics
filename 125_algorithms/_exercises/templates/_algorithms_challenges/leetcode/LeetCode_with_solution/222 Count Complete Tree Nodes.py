"""
Given a complete binary tree, count the number of nodes.

In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""
__author__ = 'Daniel'


c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..

    ___ __repr__
        r.. repr(val)


c_ Solution:
    ___ countNodes(self, root):
        """
        O((lg n)^2)
        """
        __ n.. root:
            r.. 0
        h = get_height(root)
        h_r = get_height(root.right)
        __ h __ h_r+1:
            r.. 2**(h-1)-1+1+countNodes(root.right)  # left_tree nodes + root + right_tree nodes
        ____:
            r.. 2**(h-2)-1+1+countNodes(root.left)  # right_tree nodes + root + left_tree nodes

    ___ get_height(self, cur):
        h = 0  # depth starting from 0
        w.... cur:
            h += 1
            cur = cur.left

        r.. h


c_ Solution_TLE:
    ___ - ):
        depth = 0  # depth starts from 1
        cnt = 0
        stopped = F..

    ___ countNodes(self, root):
        """

        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0
        get_depth(root)
        fanthom(root, 1)
        r.. 2**(depth-1)-1+cnt

    ___ get_depth(self, root):
        depth += 1
        __ root.left:
            get_depth(root.left)

    ___ fanthom(self, root, depth):
        __ stopped:
            r..

        __ n.. root.left a.. n.. root.left:
            __ depth __ depth:
                cnt += 1
            ____:
                stopped = T..
            r..

        __ root.left:
            fanthom(root.left, depth+1)
        __ root.right:
            fanthom(root.right, depth+1)

    ___ countNodes_TLE(self, root):
        """
        Brute Force

        :type root: TreeNode
        :rtype: int
        """
        __ n.. root:
            r.. 0

        r.. 1+countNodes(root.left)+countNodes(root.right)


__ __name__ __ "__main__":
    p..
