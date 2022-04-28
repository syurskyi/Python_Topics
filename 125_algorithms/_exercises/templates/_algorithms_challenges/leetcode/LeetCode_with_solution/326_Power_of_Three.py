c_ Solution o..
    # def isPowerOfThree(self, n):
    #     """
    #     :type n: int
    #     :rtype: bool
    #     """
    #     import math
    #     if n <= 0:
    #         return False
    #     # use round to check
    #     log_res = round(math.log(n, 3), 10)
    #     if log_res - int(log_res) > 0:
    #         return False
    #     return True

    ___ isPowerOfThree  n):
        max3pow = 1162261467
        __ n <= 0 or n > max3pow:
            r_ False
        r_ max3pow % n __ 0