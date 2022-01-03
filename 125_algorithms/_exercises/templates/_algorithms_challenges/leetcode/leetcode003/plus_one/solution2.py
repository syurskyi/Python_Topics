c_ Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    ___ plusOne(self, digits):
        # In-place version
        digits.reverse()
        d = digits[0]
        digits[0] = (d + 1) % 10
        carry = (d + 1) / 10
        ___ i, d __ e..(digits[1:], 1):
            digits[i] = (d + carry) % 10
            carry = (d + carry) / 10
        __ carry __ 1:
            digits.a..(1)
        digits.reverse()
        r.. digits
