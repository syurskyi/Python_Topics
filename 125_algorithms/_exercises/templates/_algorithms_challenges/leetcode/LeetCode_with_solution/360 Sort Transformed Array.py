"""
Premium Question
"""
__author__ = 'Daniel'

_______ bisect


c_ Solution(o..):
    ___ sortTransformedArray  nums, a, b, c):
        """
        Key points:
        Quadratic function

        Pitfalls:
        1. case when a = 0
        2. whether need to reverse the string
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        __ a __ 0:
            ret = map(l.... x: f(x, a, b, c), nums)
            r.. ret __ b > 0 ____ ret[::-1]

        mid = - f__(b) / (2*a)
        ri = bisect.bisect_left(nums, mid)
        le = ri - 1
        ret    # list
        w.... le >= 0 a.. ri < l..(nums) a.. le < ri:
            f_le = f(nums[le], a, b, c)
            f_ri = f(nums[ri], a, b, c)
            __ a > 0 a.. f_le < f_ri o. a < 0 a.. f_le > f_ri:
                ret.a..(f_le)
                le -= 1
            ____:
                ret.a..(f_ri)
                ri += 1

        w.... le >= 0:
            ret.a..(f(nums[le], a, b, c))
            le -= 1
        w.... ri < l..(nums):
            ret.a..(f(nums[ri], a, b, c))
            ri += 1

        r.. ret __ a > 0 ____ ret[::-1]

    ___ f  x, a, b, c):
        r.. a * (x ** 2) + b * x + c


__ _______ __ _______
    ... Solution().sortTransformedArray([-4, -2, 2, 4], -1, 3, 5) __ [-23, -5, 1, 7]