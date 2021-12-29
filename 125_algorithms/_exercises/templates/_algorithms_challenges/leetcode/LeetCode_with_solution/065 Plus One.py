"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""
__author__ = 'Danyang'


class Solution(object):
    ___ plusOne(self, digits):
        """
        Math

        Basics of all other questions like adding, multiplying.
        :param digits: a list of integer digits
        :return: a list of integer digits
        """
        ___ i __ xrange(l..(digits)-1, -1, -1):
            digits[i] += 1
            __ digits[i] < 10:
                r.. digits
            ____:
                digits[i] -= 10

        # MSB
        digits.insert(0, 1)
        r.. digits

    ___ plusOne(self, digits):
        """
        Good habit to reverse it first
        :param digits:
        :return:
        """
        digits.reverse()

        digits[0] += 1
        carry = 0
        ___ i __ xrange(l..(digits)):  # for ind, val in enumerate(digits):
            digits[i] += carry
            __ digits[i] > 9:
                digits[i] -= 10
                carry = 1
            ____:
                carry = 0
                break

        __ carry:
            digits.a..(1)

        digits.reverse()
        r.. digits


__ __name__ __ "__main__":
    digits = [9]
    ... Solution().plusOne(digits) __ [1, 0]