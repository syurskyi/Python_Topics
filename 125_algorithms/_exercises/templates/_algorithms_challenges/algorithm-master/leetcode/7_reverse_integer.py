class Solution:
    ___ reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        __ not x:
            return ans

        INT_MAX = 0x7FFFFFFF
        _x = x __ x > 0 else -x

        while _x:
            ans = ans * 10 + _x % 10
            _x //= 10

        __ ans >= INT_MAX:
            return 0

        return ans __ x > 0 else -ans
