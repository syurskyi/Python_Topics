"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be
built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
____ c.. _______ defaultdict

__author__ = 'Daniel'


c_ Solution(object):
    ___ longestPalindrome  s):
        """
        :type s: str
        :rtype: int
        """
        c = defaultdict(i..)
        ___ elt __ s:
            c[elt] += 1

        ret = 0
        ___ v __ c.v..
            ret += (v/2) * 2

        __ any(map(l.... x: x % 2 __ 1, c.v..:
            ret += 1

        r.. ret


__ _______ __ _______
    ... Solution().longestPalindrome("abccccdd") __ 7
