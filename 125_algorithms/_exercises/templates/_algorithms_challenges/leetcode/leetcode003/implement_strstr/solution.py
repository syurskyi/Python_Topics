"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
"""

c_ Solution(object):
    ___ strStr  haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = l..(haystack)
        m = l..(needle)
        ___ i __ r..(n + 1 - m):
            matched = T..
            ___ k __ r..(m):
                __ haystack[i + k] != needle[k]:
                    matched = F..
                    break
            __ matched:
                r.. i
        r.. -1
