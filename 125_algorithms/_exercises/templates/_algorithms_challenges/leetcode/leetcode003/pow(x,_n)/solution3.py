c_ Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    ___ pow  x, n
        __ n __ 0:
            r.. 1.0
        ____ n __ 1:
            r.. x
        ____ n < 0:
            r.. 1.0 / pow(x, -n)
        ____
            r.. pow(x, n / 2) * pow(x, n - n / 2)
