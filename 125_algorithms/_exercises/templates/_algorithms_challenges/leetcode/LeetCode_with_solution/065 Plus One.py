"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""
__author__ 'Danyang'


c_ Solution(o..
    ___ plusOne  d..
        """
        Math

        Basics of all other questions like adding, multiplying.
        :param digits: a list of integer digits
        :return: a list of integer digits
        """
        ___ i __ x..(l..(d..)-1, -1, -1
            d..[i] += 1
            __ d..[i] < 10:
                r.. d..
            ____
                d..[i] -_ 10

        # MSB
        d...insert(0, 1)
        r.. d..

    ___ plusOne  d..
        """
        Good habit to reverse it first
        :param digits:
        :return:
        """
        d...r..

        d..[0] += 1
        carry 0
        ___ i __ x..(l..(d..:  # for ind, val in enumerate(digits):
            d..[i] += carry
            __ d..[i] > 9:
                d..[i] -_ 10
                carry 1
            ____
                carry 0
                _____

        __ carry:
            d...a..(1)

        d...r..
        r.. d..


__ _______ __ _______
    d.. [9]
    ... Solution().plusOne(d..) __ [1, 0]