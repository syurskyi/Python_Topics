"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
"""

class Solution(object):
    ___ strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

          needle: |       n       |
        haystack: |   n - m   | m |
        """
        n = l..(haystack)
        m = l..(needle)
        ___ i __ r..(n + 1 - m):
            ___ k __ r..(m):
                __ haystack[i + k] != needle[k]:
                    break
            ____:
                r.. i
        r.. -1
