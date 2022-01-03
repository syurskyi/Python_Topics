"""
Premium Question
https://leetcode.com/problems/palindrome-permutation/
"""
____ collections _______ defaultdict

__author__ = 'Daniel'


c_ Solution(object):
    ___ canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = defaultdict(int)
        ___ c __ s:
            m[c] += 1

        once = F..
        ___ v __ m.v..
            __ v % 2 __ 1:
                __ once:
                    r.. F..
                once = T..

        r.. T..