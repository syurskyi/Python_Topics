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
                r_ self.pow(x * x, n / 2)
            ____
                r_ self.pow(x * x, (n - 1) / 2) * x
