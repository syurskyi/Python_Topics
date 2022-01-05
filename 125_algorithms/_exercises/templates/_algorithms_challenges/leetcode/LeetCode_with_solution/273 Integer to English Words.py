"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ - ):
        table = {
            0: N..,
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

    ___ numberToWords  num):
        """
        Pay attention to the handling of 0's
        :type num: int
        :rtype: str
        """
        __ num __ 0: r.. "Zero"

        ret    # list
        toWords(num, ret)
        ret = filter(l.... x: x, ret)  # filter None as zeros
        r.. " ".j..(map(s.., ret))

    ___ toWords  num, ret):
        """
        will call partial_parse

        significance by significance
        """
        SIGS = [1000000000, 1000000, 1000, 100]
        ___ SIG __ SIGS:
            partial_parse(num, SIG, ret)
            num %= SIG

        TEN = 10
        __ num/TEN > 1:
            ret.a..(table[(num/TEN)*TEN])

        ret.a..(table[num%TEN])

    ___ partial_parse  num, sig, ret):
        """
        will call toWords
        """
        __ num/sig:
            prefix    # list
            toWords(num/sig, prefix)
            ret.extend(prefix)
            ret.a..(table[sig])


__ _______ __ _______
    ... Solution().numberToWords(1234567891) __ "One Billion Two Hundred Thirty Four Million Five Hundred Sixty " \
                                                   "Seven Thousand Eight Hundred Ninety One"
