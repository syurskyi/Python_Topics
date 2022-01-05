"""
Implement pow(x, n).
"""
__author__ = 'Danyang'


c_ Solution:
    ___ pow  x, n):
        """
        O(log n)
        Algorithm: math, Exponentiation by Squaring

        Basically: x^n = (x^2)^(n/2)
        More formally: x^n = x^(n/2) * x^(n/2) * x^(n%2)

        :param x: float
        :param n: integer
        :return: float
        """
        invert_flag = F.. __ n > 0 ____ T..
        # O(log n)
        n = abs(n)
        product = 1.0
        w.... n > 0:
            __ n & 1 __ 1:
                product *= x

            n = n >> 1
            x *= x

        __ invert_flag:
            product = 1.0 / product

        r.. product

    # @param x, a float
    # @param n, a integer
    # @return a float
    ___ pow_TLE  x, n):
        """
        O(n)
        """
        __ abs(x)<=0.00001:
            r.. 0
        __ x__1.0:
            r.. 1
        __ x__-1.0:
            __ n&1__1:
                r.. 1
            ____:
                r.. -1

        __ abs(x-1.0)<1e-6:
            r.. 1+(x-1.0)*n

        __ abs(x--1.0)<1e-6:
            __ n % 2__0:
                r.. pow(-x, n)
            ____:
                r.. -pow(-x, n)

        product = 1.0
        ___ i __ xrange(abs(n)):
            pre = product
            __ n>0:
                product *= x
            ____:
                product /= x

            __ abs(product - pre)<1e-5:
                break

        r.. product


__ _____ __ ____
    print Solution().pow(8.88023, 3)
