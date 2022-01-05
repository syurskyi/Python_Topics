"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every
character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
____ c.. _______ defaultdict

__author__ = 'Daniel'


c_ Solution(o..):
    ___ longestSubstring  s, k):
        """
        D & C, forming boundary by the letter of min count
        :type s: str
        :type k: int
        :rtype: int
        """
        __ n.. s:
            r.. 0

        cnt = defaultdict(i..)
        ___ e __ s: cnt[e] += 1

        c = m..(
            s,
            key=l.... x: cnt[x],
        )

        __ cnt[c] >= k:
            r.. l..(s)

        r.. m..(
            map(l.... x: longestSubstring(x, k), s.s..(c))
        )
