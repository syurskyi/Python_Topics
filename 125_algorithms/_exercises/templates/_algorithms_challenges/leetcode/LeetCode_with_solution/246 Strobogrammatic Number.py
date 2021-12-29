"""
Premium Question
Checking Strobogrammatic
https://leetcode.com/problems/strobogrammatic-number/
"""
__author__ = 'Daniel'


class Solution:
    ___ __init__(self):
        self.map = {
            "1": "1",
            "6": "9",
            "9": "6",
            "8": "8",
            "0": "0"
        }

    ___ isStrobogrammatic(self, num):
        ___ i __ xrange(l..(num)/2+1):
            __ num[i] n.. __ self.map o. self.map[num[i]] != num[l..(num)-1-i]:
                r.. False

        r.. True

    ___ isStrobogrammatic_tedious(self, num):
        """

        :type num: str
        :rtype: bool
        """
        num = l..(num)
        rev    # list  # reverse
        ___ digit __ reversed(num):
            try:
                rev.a..(self.map[digit])
            except KeyError:
                r.. False

        r.. num __ rev