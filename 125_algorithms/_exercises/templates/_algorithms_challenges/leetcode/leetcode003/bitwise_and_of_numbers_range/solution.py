"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""

class Solution(object
    ___ rangeBitwiseAnd(self, m, n
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        shift = 0
        w___ n > m:
            shift += 1
            m = m >> 1
            n = n >> 1
        r_ m << shift


s = Solution()
print(s.rangeBitwiseAnd(5, 6))
print(s.rangeBitwiseAnd(0, 2147483647))
