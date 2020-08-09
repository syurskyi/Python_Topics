class Solution:
    ___ sqrt(self, x
        """
        :type x: int
        :rtype: int
        """
        __ not x or x <= 1:
            r_ x

        left, right = 0, x

        w___ left + 1 < right:
            mid = (left + right) // 2
            square = mid * mid

            __ square __ x:
                r_ mid

            __ square < x:
                left = mid
            ____
                right = mid

        r_ left
