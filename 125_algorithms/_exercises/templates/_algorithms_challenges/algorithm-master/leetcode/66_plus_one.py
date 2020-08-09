class Solution:
    ___ plusOne(self, digits
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = []

        __ not digits:
            r_ ans

        carry = 1

        ___ i in range(le.(digits) - 1, -1, -1
            carry += digits[i]
            ans.append(carry % 10)
            carry //= 10

        __ carry:
            ans.append(carry)

        ans.reverse()

        r_ ans


class Solution:
    ___ plusOne(self, digits
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        __ not digits:
            r_ []

        carry = 0
        digits[-1] += 1

        ___ i in range(le.(digits) - 1, -1, -1
            carry += digits[i]
            digits[i] = carry % 10
            carry //= 10

        __ carry:
            digits.append(carry)

            ___ i in range(le.(digits) - 1, 0, -1
                digits[i], digits[i - 1] = digits[i - 1], digits[i]

        r_ digits
