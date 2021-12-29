"""
Premium Question
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution:
    ___ groupStrings(self, strings):
        """

        :type strings: list[str]
        :rtype: list[list[str]]
        """
        hm = defaultdict(list)
        for s in strings:
            __ len(s) == 1:
                hm[0].append(s)
            else:
                lst = []
                for i in xrange(1, len(s)):
                    lst.append((ord(s[i])-ord(s[i-1]))%26)
                hm[tuple(lst)].append(s)

        return map(sorted, hm.values())