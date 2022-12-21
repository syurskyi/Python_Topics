c_ Solution:
    # def myPow(self, x, n):
    #     """
    #     :type x: float
    #     :type n: int
    #     :rtype: float
    #     """
    #     if n == 0:
    #         return 1
    #     temp = pow(x, n / 2)
    #     if n % 2 == 0:
    #         return temp * temp
    #     else:
    #         return temp * temp * x

    ___ myPow  x, n
        # https://leetcode.com/discuss/93413/iterative-log-n-solution-with-clear-explanation
        # 9 = 2^3 + 2^0 = 1001
        # x^9 = x^(2^3)*x(2^0)
        # multiple x^i when i place is 1
        __ n __ 0:
            r_ 1
        res ,curr = 1, abs(n)
        w.. curr > 0:
            __ curr & 1 __ 1:
                res *= x
            curr >>= 1
            x *= x
        __ n < 0:
            r_ 1 / res
        r_  res
