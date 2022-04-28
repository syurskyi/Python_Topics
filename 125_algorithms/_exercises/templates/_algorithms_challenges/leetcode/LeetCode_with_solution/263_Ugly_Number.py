c_ Solution o..
    # def isUgly(self, num):
    #     """
    #     :type num: int
    #     :rtype: bool
    #     """
    #     if num <= 0:
    #         return False
    #     if num <= 6:
    #         return True
    #     while num % 2 == 0:
    #         num //= 2
    #     while num % 3 == 0:
    #         num //= 3
    #     while num % 5 == 0:
    #         num //= 5
    #     if num == 1:
    #         return True
    #     return False
    ___ isUgly  num):
        __ num <= 0:
            r_ False
        divisors = [2, 3, 5]
        ___ d __ divisors:
            w.. num % d __ 0:
                num /= d
        r_ num __ 1

__ ____ __ ____
    s  ?
    print s.isUgly(-2147483648)
