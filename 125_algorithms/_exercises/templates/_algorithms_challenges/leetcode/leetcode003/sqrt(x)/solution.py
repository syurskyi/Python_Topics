class Solution:
    # @param x, an integer
    # @return an integer
    ___ sqrt(self, x
        left = 0
        right = x
        w___ left <= right:
            mid = left + (right - left) / 2
            square = mid * mid
            __ square __ x:
                r_ mid
            ____ square < x:
                left = mid + 1
            ____
                right = mid - 1
        r_ (left + right) / 2
