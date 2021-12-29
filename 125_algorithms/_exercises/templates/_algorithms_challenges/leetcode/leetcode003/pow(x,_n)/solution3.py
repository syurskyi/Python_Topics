class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    ___ pow(self, x, n):
        __ n __ 0:
            r.. 1.0
        ____ n __ 1:
            r.. x
        ____ n < 0:
            r.. 1.0 / self.pow(x, -n)
        ____:
            r.. self.pow(x, n / 2) * self.pow(x, n - n / 2)
