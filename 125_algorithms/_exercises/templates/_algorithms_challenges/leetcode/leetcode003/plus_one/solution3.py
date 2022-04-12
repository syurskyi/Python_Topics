"""
Given a non-negative number represented as an array of digits, plus one to the
number.

The digits are stored such that the most significant digit is at the head of
the list.
"""

c_ Solution(o..
    ___ plusOne  d..
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d.. d..[::-1]
        n l..(d..)
        temp 0
        # Treat "plus one" as the initial carry being 1
        carry 1
        i 0
        res    # list
        w.... i < n o. carry > 0
            temp 0
            __ i < n:
                temp += d..[i]
            __ carry > 0
                temp += carry
            digit temp % 10
            carry temp / 10
            res.a..(digit)
            i += 1
        r.. res[::-1]

a0    # list
a1 [3, 3, 5]
a2 [4, 9, 9]
a3 [9, 9, 9]
s Solution()
print s.plusOne(a0)
print s.plusOne(a1)
print s.plusOne(a2)
print s.plusOne(a3)
