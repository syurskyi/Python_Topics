class Solution:
    ___ hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        __ not n:
            return ans

        while n != 0:
            n = n & (n - 1)
            ans += 1

        return ans
