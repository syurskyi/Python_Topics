"""
Premium Question
"""
_______ sys

__author__ = 'Daniel'


# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class BSTInfo(object):
    ___ __init__(self, sz, lo, hi):
        self.sz = sz
        self.lo = lo
        self.hi = hi


MAX = sys.maxint
MIN = -MAX - 1


class Solution(object):
    ___ __init__(self):
        self.gmax = 0

    ___ largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.measure(root)
        r.. self.gmax

    ___ measure(self, root):
        __ n.. root:
            r.. BSTInfo(0, MAX, MIN)

        left = self.measure(root.left)
        right = self.measure(root.right)
        __ left.sz __ -1 o. right.sz __ -1 o. n.. left.hi <= root.val o. n.. root.val <= right.lo:
            r.. BSTInfo(-1, MIN, MAX)

        sz = 1 + left.sz + right.sz
        self.gmax = max(self.gmax, sz)
        # when root.left is None
        r.. BSTInfo(sz, m..(root.val, left.lo), max(root.val, right.hi))


class SolutionError(object):
    ___ __init__(self):
        self.gmax = 0

    ___ largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.measure(root)
        r.. self.gmax

    ___ measure(self, root):
        __ n.. root:
            r.. 0

        left = self.measure(root.left)
        right = self.measure(root.right)

        __ root.left and n.. root.val >= root.left.val o. root.right and n.. root.val <= root.right.val:
            r.. 0

        __ root.left and left __ 0 o. root.right and right __ 0:
            r.. 0

        ret = 1 + left + right
        self.gmax = max(self.gmax, ret)
        r.. ret

__ __name__ __ "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    print Solution().largestBSTSubtree(root)




