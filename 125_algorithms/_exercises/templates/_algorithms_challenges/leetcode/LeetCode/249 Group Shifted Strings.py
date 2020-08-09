"""
Premium Question
"""
from collections ______ defaultdict

__author__ = 'Daniel'


class Solution:
    ___ groupStrings(self, strings
        """

        :type strings: list[str]
        :rtype: list[list[str]]
        """
        hm = defaultdict(list)
        for s in strings:
            __ le.(s) __ 1:
                hm[0].append(s)
            ____
                lst = []
                for i in xrange(1, le.(s)):
                    lst.append((ord(s[i])-ord(s[i-1]))%26)
                hm[tuple(lst)].append(s)

        r_ map(sorted, hm.values())