c_ Solution:
    # def mySqrt(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     if x == 0:
    #         return 0
    #     low = 0
    #     high = x
    #     last = x
    #     while high >= low:
    #         mid = (low + high) / 2
    #         temp = mid * mid
    #         if temp == x:
    #             return mid
    #         elif temp < x:
    #             low = mid + 1
    #             last = mid
    #         else:
    #             high = mid - 1
    #     return last

    ___ mySqrt  x
        # sqrt(x) = 2 * sqrt(x / 4) for n % 4 == 0
        # sqrt(x) = 1 + 2 * sqrt(x / 4) for n % 4 != 0
        __ x __ 0:
            r_ 0
        __ x < 4:
            r_ 1
        res = 2 * mySqrt(x / 4)
        # (res + 1) * (res + 1) >= 0 for avoiding overflow
        __ (res + 1) * (res + 1) <= x and (res + 1) * (res + 1) >= 0:
            r_ res + 1
        r_  res