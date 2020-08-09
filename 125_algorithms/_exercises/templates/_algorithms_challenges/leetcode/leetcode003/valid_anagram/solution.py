"""
Given two strings s and t, write a function to determine if t is an anagram of
s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""


class Solution(object
    ___ isAnagram(self, s, t
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        __ le.(s) != le.(t
            r_ False
        d = {}
        for c in s:
            __ c in d:
                d[c] += 1
            ____
                d[c] = 1
        for c in t:
            __ c not in d:
                r_ False
            ____
                d[c] -= 1
            __ d[c] < 0:
                r_ False
        r_ True


s = Solution()
print(s.isAnagram("aacc", "ccac"))
print(s.isAnagram("abcd", "bcda"))
