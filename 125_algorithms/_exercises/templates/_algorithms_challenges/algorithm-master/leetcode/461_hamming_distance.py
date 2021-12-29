class Solution:
    ___ hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        ans = 0

        __ not n:
            return ans

        while n != 0:
            n = n & (n - 1)
            ans += 1

        return ans
