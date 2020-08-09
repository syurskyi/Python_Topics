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
from collections ______ defaultdict


class Solution:
    ___ countSubstrings(self, s
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
        F = defaultdict(lambda: defaultdict(bool))
        n = le.(s)
        ___ i in range(n
            F[i][i] = True
            F[i][i+1] = True

        ___ i in range(n-1, -1, -1
            ___ j in range(i+2, n+1
                __ s[i] __ s[j-1]:
                    F[i][j] = F[i+1][j-1]
                ____
                    F[i][j] = False

        r_ su.(
            1
            ___ i in range(n)
            ___ j in range(i+1, n+1)
            __ F[i][j]
        )


__ __name__ __ "__main__":
    assert Solution().countSubstrings("aaa") __ 6
