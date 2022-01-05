"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding
column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    AZ -> 26 + 26 = 52
    BA -> 52 + 1 = 53
"""

c_ Solution(o..):
    ___ titleToNumber  s):
        """
        :type s: str
        :rtype: int
        """
        d    # dict
        res = 0
        ___ i, k __ e..(r..(o..('A'), o..('Z') + 1), start=1):
            d[chr(k)] = i
        j = 0
        ___ c __ s[::-1]:
            res += d[c] * (26 ** j)
            j += 1
        r.. res


s = Solution()
print s.titleToNumber('A')
print s.titleToNumber('B')
print s.titleToNumber('AA')
print s.titleToNumber('BA')
print s.titleToNumber('AAA')
