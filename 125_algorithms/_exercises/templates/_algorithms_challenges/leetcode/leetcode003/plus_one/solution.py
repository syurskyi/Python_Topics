class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    ___ plusOne(self, digits):
        digits.reverse()
        res    # list
        t = (digits[0] + 1) % 10
        carry = (digits[0] + 1) / 10
        res.a..(t)
        ___ d __ digits[1:]:
            t = (d + carry) % 10
            carry = (d + carry) / 10
            res.a..(t)
        __ carry __ 1:
            res.a..(1)
        res.reverse()
        r.. res
