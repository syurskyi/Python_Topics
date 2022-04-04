"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

c_ Solution(o..
    ___ isIsomorphic  s, t
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d    # dict
        ___ i, c __ e..(s
            __ c n.. __ d:
                d[c] = t[i]
            ____
                __ d[c] != t[i]:
                    r.. F..
        d    # dict
        ___ i, c __ e..(t
            __ c n.. __ d:
                d[c] = s[i]
            ____
                __ d[c] != s[i]:
                    r.. F..
        r.. T..


s = Solution()
f = s.isIsomorphic
print(f('ab', 'aa'
print(f('egg', 'add'
print(f('foo', 'bar'
print(f('paper', 'title'
