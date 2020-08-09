class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    ___ plusOne(self, digits
        # In-place version
        digits.reverse()
        d = digits[0]
        digits[0] = (d + 1) % 10
        carry = (d + 1) / 10
        for i, d in enumerate(digits[1:], 1
            digits[i] = (d + carry) % 10
            carry = (d + carry) / 10
        __ carry __ 1:
            digits.append(1)
        digits.reverse()
        r_ digits
