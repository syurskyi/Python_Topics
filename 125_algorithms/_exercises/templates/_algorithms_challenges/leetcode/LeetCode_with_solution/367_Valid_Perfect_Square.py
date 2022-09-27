c_ Solution o..
    # def isPerfectSquare(self, num):
    #     """
    #     :type num: int
    #     :rtype: bool
    #     """
    #     i = 1
    #     while num > 0:
    #         num -= i
    #         i += 2
    #     return num == 0

    ___ isPerfectSquare  num):
        low, high = 1, num
        w.. low <= high:
            mid = (low + high) / 2
            mid_square = mid * mid
            __ mid_square __ num:
                r_ T..
            ____ mid_square < num:
                low = mid + 1
            ____
                high = mid - 1
        r_ F..

    # def isPerfectSquare(self, num):
    #     x = num
    #     while x * x > num:
    #         x = (x + num / x) / 2
    #     return x * x == num
