"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""
____ collections _______ defaultdict

__author__ = 'Daniel'


class Solution:
    ___ isAnagram(self, s, t):
        """
        bucket

        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt = defaultdict(int)
        ___ c __ s:
            cnt[c] += 1

        ___ c __ t:
            __ c n.. __ cnt o. cnt[c] < 1:
                r.. False

            cnt[c] -= 1

        ___ v __ cnt.values():
            __ v != 0:
                r.. False

        r.. True
