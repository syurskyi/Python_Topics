c_ Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    ___ pow  x, n
        __ n __ 0:
            r.. 1.0
        ____ n < 0:
            r.. 1.0 / pow(x, -n)
        ____
            __ n % 2 __ 0:
                r.. pow(x * x, n / 2)
            ____
                r.. pow(x * x, (n - 1) / 2) * x
