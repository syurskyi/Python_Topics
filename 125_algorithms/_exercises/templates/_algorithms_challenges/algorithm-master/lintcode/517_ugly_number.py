class Solution:
    ___ isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        __ n.. num:
            r.. False
        __ num __ 1:
            r.. True

        ___ factor __ (
            125, 27, 8,
            5, 3, 2,
        ):
            w.... num % factor __ 0:
                num //= factor

            __ num __ 1:
                r.. True

        r.. num __ 1
