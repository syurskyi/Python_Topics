class Solution:
    ___ sqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        __ not x or x <= 1:
            return x

        left, right = 0, x

        while left + 1 < right:
            mid = (left + right) // 2
            square = mid * mid

            __ square == x:
                return mid

            __ square < x:
                left = mid
            else:
                right = mid

        return left
