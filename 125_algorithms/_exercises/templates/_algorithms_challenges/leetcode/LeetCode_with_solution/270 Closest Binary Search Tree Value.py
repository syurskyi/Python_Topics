"""
Premium Question
"""
_______ sys

__author__ = 'Daniel'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution(object):
    ___ closestValue(self, root, target):
        """
        Divide the problem into 2 parts:
        1. find the value just smaller than target
        2. find the value just larger than target
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        lo = [-sys.float_info.max]
        self.find(root, target, lo, True)
        hi = [sys.float_info.max]
        self.find(root, target, hi, False)
        __ hi[0] - target < target - lo[0]:
            r.. int(hi[0])
        ____:
            r.. int(lo[0])

    ___ find(self, root, target, ret, lower=True):
        __ n.. root:
            r..

        __ root.val __ target:
            ret[0] = root.val
            r..

        __ root.val < target:
            __ lower: ret[0] = max(ret[0], root.val)
            self.find(root.right, target, ret, lower)
        ____:
            __ n.. lower: ret[0] = m..(ret[0], root.val)
            self.find(root.left, target, ret, lower)


__ __name__ __ "__main__":
    ... Solution().closestValue(TreeNode(2147483647), 0.0) __ 2147483647
