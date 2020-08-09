class Solution:
    ___ isUgly(self, num
        """
        :type num: int
        :rtype: bool
        """
        __ not num:
            r_ False
        __ num __ 1:
            r_ True

        ___ factor in (
            125, 27, 8,
            5, 3, 2,

            w___ num % factor __ 0:
                num //= factor

            __ num __ 1:
                r_ True

        r_ num __ 1
