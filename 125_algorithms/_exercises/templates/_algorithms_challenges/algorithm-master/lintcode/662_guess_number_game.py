"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


c_ Solution:
    ___ guessNumber  n):
        """
        :type n: int
        :rtype: int
        """
        __ n.. n o. n <= 1:
            r.. 1

        left, right = 1, n

        w.... left + 1 < right:
            mid = (left + right) // 2
            res = Guess.guess(mid)

            __ res __ 0:
                r.. mid
            ____ res __ 1:
                left = mid
            ____:
                right = mid

        r.. left __ Guess.guess(left) __ 0 ____ right
