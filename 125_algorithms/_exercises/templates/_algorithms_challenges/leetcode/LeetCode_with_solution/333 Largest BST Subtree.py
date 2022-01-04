"""
Premium Question
"""
_______ sys

__author__ = 'Daniel'


# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ BSTInfo(object):
    ___ - , sz, lo, hi):
        sz = sz
        lo = lo
        hi = hi


MAX = sys.maxint
MIN = -MAX - 1


c_ Solution(object):
    ___ - ):
        gmax = 0

    ___ largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        measure(root)
        r.. gmax

    ___ measure(self, root):
        __ n.. root:
            r.. BSTInfo(0, MAX, MIN)

        left = measure(root.left)
        right = measure(root.right)
        __ left.sz __ -1 o. right.sz __ -1 o. n.. left.hi <= root.val o. n.. root.val <= right.lo:
            r.. BSTInfo(-1, MIN, MAX)

        sz = 1 + left.sz + right.sz
        gmax = max(gmax, sz)
        # when root.left is None
        r.. BSTInfo(sz, m..(root.val, left.lo), max(root.val, right.hi))


c_ SolutionError(object):
    ___ - ):
        gmax = 0

    ___ largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        measure(root)
        r.. gmax

    ___ measure(self, root):
        __ n.. root:
            r.. 0

        left = measure(root.left)
        right = measure(root.right)

        __ root.left a.. n.. root.val >= root.left.val o. root.right a.. n.. root.val <= root.right.val:
            r.. 0

        __ root.left a.. left __ 0 o. root.right a.. right __ 0:
            r.. 0

        ret = 1 + left + right
        gmax = max(gmax, ret)
        r.. ret

__ _______ __ _______
    root = TreeNode(1)
    root.left = TreeNode(2)
    print Solution().largestBSTSubtree(root)




