"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""
____ c.. _______ d..

__author__ = 'Daniel'


c_ Solution:
    ___ isAnagram  s, t
        """
        bucket

        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt = d..(i..)
        ___ c __ s:
            cnt[c] += 1

        ___ c __ t:
            __ c n.. __ cnt o. cnt[c] < 1:
                r.. F..

            cnt[c] -_ 1

        ___ v __ cnt.v..
            __ v != 0:
                r.. F..

        r.. T..
