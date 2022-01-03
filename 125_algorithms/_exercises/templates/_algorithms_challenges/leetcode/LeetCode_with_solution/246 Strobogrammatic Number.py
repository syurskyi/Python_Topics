"""
Premium Question
Checking Strobogrammatic
https://leetcode.com/problems/strobogrammatic-number/
"""
__author__ = 'Daniel'


c_ Solution:
    ___ - ):
        map = {
            "1": "1",
            "6": "9",
            "9": "6",
            "8": "8",
            "0": "0"
        }

    ___ isStrobogrammatic(self, num):
        ___ i __ xrange(l..(num)/2+1):
            __ num[i] n.. __ map o. map[num[i]] != num[l..(num)-1-i]:
                r.. F..

        r.. T..

    ___ isStrobogrammatic_tedious(self, num):
        """

        :type num: str
        :rtype: bool
        """
        num = l..(num)
        rev    # list  # reverse
        ___ digit __ r..(num):
            try:
                rev.a..(map[digit])
            except KeyError:
                r.. F..

        r.. num __ rev