"""
Given two strings s and t, write a function to determine if t is an anagram of
s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""


class Solution(object):
    ___ isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ l..(s) != l..(t):
            r.. False
        d = {}
        ___ c __ s:
            __ c __ d:
                d[c] += 1
            ____:
                d[c] = 1
        ___ c __ t:
            __ c n.. __ d:
                r.. False
            ____:
                d[c] -= 1
            __ d[c] < 0:
                r.. False
        r.. True


s = Solution()
print(s.isAnagram("aacc", "ccac"))
print(s.isAnagram("abcd", "bcda"))
