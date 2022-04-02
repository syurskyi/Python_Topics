c_ Solution:
    ___ sqrt  x
        """
        :type x: int
        :rtype: int
        """
        __ n.. x o. x <= 1:
            r.. x

        left, right = 0, x

        w.... left + 1 < right:
            mid = (left + right) // 2
            square = mid * mid

            __ square __ x:
                r.. mid

            __ square < x:
                left = mid
            ____:
                right = mid

        r.. left
