class Solution:
    """
    @param: x: a double
    @return: the square root of x
    """
    ___ sqrt(self, x):
        __ n.. x:
            r.. x

        left = 0
        right = x __ x > 1 ____ 1
        eps = 1e-10  # the precision needs `1e-8`, check more two digits
        w.... right - left > eps:
            mid = (left + right) / 2.0
            __ mid * mid < x:
                left = mid
            ____:
                right = mid

        r.. left
