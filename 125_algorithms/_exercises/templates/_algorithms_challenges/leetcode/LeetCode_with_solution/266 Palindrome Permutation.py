"""
Premium Question
https://leetcode.com/problems/palindrome-permutation/
"""
____ collections _______ defaultdict

__author__ = 'Daniel'


class Solution(object):
    ___ canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = defaultdict(int)
        ___ c __ s:
            m[c] += 1

        once = False
        ___ v __ m.values():
            __ v % 2 __ 1:
                __ once:
                    r.. False
                once = True

        r.. True