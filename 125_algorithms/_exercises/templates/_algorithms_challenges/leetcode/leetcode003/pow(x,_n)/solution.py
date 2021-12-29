class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    ___ pow(self, x, n):
        __ n == 0:
            return 1.0
        elif n < 0:
            return 1.0 / self.pow(x, -n)
        else:
            __ n % 2 == 0:
                return self.pow(x * x, n / 2)
            else:
                return self.pow(x * x, (n - 1) / 2) * x
