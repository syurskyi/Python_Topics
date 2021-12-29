class Solution:
    ___ plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans    # list

        __ n.. digits:
            r.. ans

        carry = 1

        ___ i __ r..(l..(digits) - 1, -1, -1):
            carry += digits[i]
            ans.a..(carry % 10)
            carry //= 10

        __ carry:
            ans.a..(carry)

        ans.reverse()

        r.. ans


class Solution:
    ___ plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        __ n.. digits:
            r.. []

        carry = 0
        digits[-1] += 1

        ___ i __ r..(l..(digits) - 1, -1, -1):
            carry += digits[i]
            digits[i] = carry % 10
            carry //= 10

        __ carry:
            digits.a..(carry)

            ___ i __ r..(l..(digits) - 1, 0, -1):
                digits[i], digits[i - 1] = digits[i - 1], digits[i]

        r.. digits
