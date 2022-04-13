"""
Premium Question
"""
_______ ___

__author__ 'Daniel'


c_ TreeNode(o..
    ___ - , x
        val x
        left N..
        right N..


c_ Solution(o..
    ___ closestValue  root, target
        """
        Divide the problem into 2 parts:
        1. find the value just smaller than target
        2. find the value just larger than target
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        lo [-___.float_info.m..]
        f.. root, target, lo, T..)
        hi [___.float_info.m..]
        f.. root, target, hi, F..)
        __ hi[0] - target < target - lo[0]:
            r.. i..(hi 0
        ____
            r.. i..(lo 0

    ___ find  root, target, ret, lower=T..
        __ n.. root:
            r..

        __ root.val __ target:
            ret[0] root.val
            r..

        __ root.val < target:
            __ lower: ret[0] m..(ret[0], root.val)
            f.. root.right, target, ret, lower)
        ____
            __ n.. lower: ret[0] m..(ret[0], root.val)
            f.. root.left, target, ret, lower)


__ _______ __ _______
    ... Solution().closestValue(TreeNode(2147483647), 0.0) __ 2147483647
