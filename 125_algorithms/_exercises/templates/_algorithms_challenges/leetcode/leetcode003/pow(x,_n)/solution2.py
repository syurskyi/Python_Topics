class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    ___ pow(self, x, n
        __ n __ 0:
            r_ 1.0
        ____ n < 0:
            r_ 1.0 / self.pow(x, -n)
        ____
            __ n % 2 __ 0:
                r = self.pow(x, n / 2)
                r_ r * r
            ____
                r = self.pow(x, (n - 1) / 2)
                r_ r * r * x
