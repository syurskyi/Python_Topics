# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

c_ Solution o..
    ___ guessNumber  n
        """
        :type n: int
        :rtype: int
        """
        # binary search
        begin, end = 1, n
        w.. begin <= end:
            mid = (begin + end) / 2
            res = guess(mid)
            __ res __ 0:
                r_ mid
            ____ res > 0:
                begin = mid + 1
            ____
                end = mid - 1
