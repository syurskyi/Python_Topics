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
        __ len(s) != len(t):
            return False
        d = {}
        for c in s:
            __ c in d:
                d[c] += 1
            else:
                d[c] = 1
        for c in t:
            __ c not in d:
                return False
            else:
                d[c] -= 1
            __ d[c] < 0:
                return False
        return True


s = Solution()
print(s.isAnagram("aacc", "ccac"))
print(s.isAnagram("abcd", "bcda"))
