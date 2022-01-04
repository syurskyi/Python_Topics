#!/usr/bin/python3
"""
Given a string, your task is to count how many palindromic substrings in this
string.

The substrings with different start indexes or end indexes are counted as
different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""
____ c.. _______ defaultdict


c_ Solution:
    ___ countSubstrings(self, s):
        """
        for every s[i:j], check whether it is a palindrome
        O(n^2 * n)

        DP
        Let F[i][j] be whether s[i:j] is a palindrome
        F[i][j] = F[i+1][j-1] if s[i] == s[j-1]
                  else False

        :type s: str
        :rtype: int
        """
        F = defaultdict(l....: defaultdict(bool))
        n = l..(s)
        ___ i __ r..(n):
            F[i][i] = T..
            F[i][i+1] = T..

        ___ i __ r..(n-1, -1, -1):
            ___ j __ r..(i+2, n+1):
                __ s[i] __ s[j-1]:
                    F[i][j] = F[i+1][j-1]
                ____:
                    F[i][j] = F..

        r.. s..(
            1
            ___ i __ r..(n)
            ___ j __ r..(i+1, n+1)
            __ F[i][j]
        )


__ __name__ __ "__main__":
    ... Solution().countSubstrings("aaa") __ 6
