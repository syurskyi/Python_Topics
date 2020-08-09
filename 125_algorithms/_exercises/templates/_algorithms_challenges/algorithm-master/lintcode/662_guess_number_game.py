"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    ___ guessNumber(self, n
        """
        :type n: int
        :rtype: int
        """
        __ not n or n <= 1:
            r_ 1

        left, right = 1, n

        w___ left + 1 < right:
            mid = (left + right) // 2
            res = Guess.guess(mid)

            __ res __ 0:
                r_ mid
            ____ res __ 1:
                left = mid
            ____
                right = mid

        r_ left __ Guess.guess(left) __ 0 else right
