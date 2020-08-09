"""
Premium Question
"""
__author__ = 'Daniel'

______ bisect


class Solution(object
    ___ sortTransformedArray(self, nums, a, b, c
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
            ret = map(lambda x: self.f(x, a, b, c), nums)
            r_ ret __ b > 0 else ret[::-1]

        mid = - float(b) / (2*a)
        ri = bisect.bisect_left(nums, mid)
        le = ri - 1
        ret = []
        w___ le >= 0 and ri < le.(nums) and le < ri:
            f_le = self.f(nums[le], a, b, c)
            f_ri = self.f(nums[ri], a, b, c)
            __ a > 0 and f_le < f_ri or a < 0 and f_le > f_ri:
                ret.append(f_le)
                le -= 1
            ____
                ret.append(f_ri)
                ri += 1

        w___ le >= 0:
            ret.append(self.f(nums[le], a, b, c))
            le -= 1
        w___ ri < le.(nums
            ret.append(self.f(nums[ri], a, b, c))
            ri += 1

        r_ ret __ a > 0 else ret[::-1]

    ___ f(self, x, a, b, c
        r_ a * (x ** 2) + b * x + c


__ __name__ __ "__main__":
    assert Solution().sortTransformedArray([-4, -2, 2, 4], -1, 3, 5) __ [-23, -5, 1, 7]