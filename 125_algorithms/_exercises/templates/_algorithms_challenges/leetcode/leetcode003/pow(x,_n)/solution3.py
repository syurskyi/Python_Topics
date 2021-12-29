class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    ___ pow(self, x, n):
        __ n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n < 0:
            return 1.0 / self.pow(x, -n)
        else:
            return self.pow(x, n / 2) * self.pow(x, n - n / 2)
