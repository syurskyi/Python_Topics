"""
Premium Question
https://leetcode.com/problems/palindrome-permutation/
"""
from collections ______ defaultdict

__author__ = 'Daniel'


class Solution(object
    ___ canPermutePalindrome(self, s
        """
        :type s: str
        :rtype: bool
        """
        m = defaultdict(int)
        for c in s:
            m[c] += 1

        once = False
        for v in m.values(
            __ v % 2 __ 1:
                __ once:
                    r_ False
                once = True

        r_ True