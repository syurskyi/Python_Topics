"""
Premium Question
"""
____ collections _______ defaultdict

__author__ = 'Daniel'


c_ Solution:
    ___ groupStrings(self, strings):
        """

        :type strings: list[str]
        :rtype: list[list[str]]
        """
        hm = defaultdict(l..)
        ___ s __ strings:
            __ l..(s) __ 1:
                hm[0].a..(s)
            ____:
                lst    # list
                ___ i __ xrange(1, l..(s)):
                    lst.a..((ord(s[i])-ord(s[i-1]))%26)
                hm[tuple(lst)].a..(s)

        r.. map(s.., hm.values())