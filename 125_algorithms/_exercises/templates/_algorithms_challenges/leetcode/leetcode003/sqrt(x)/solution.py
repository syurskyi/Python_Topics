class Solution:
    # @param x, an integer
    # @return an integer
    ___ sqrt(self, x):
        left = 0
        right = x
        while left <= right:
            mid = left + (right - left) / 2
            square = mid * mid
            __ square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return (left + right) / 2
