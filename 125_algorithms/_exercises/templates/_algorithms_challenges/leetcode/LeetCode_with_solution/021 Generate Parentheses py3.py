#!/usr/bin/python3
"""
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
____ typing _______ List


c_ Solution:
    ___ generateParenthesis  n: i..) __ List[s..]:
        """
        Method 1 - backtracking
        Method 2 - dp
        Let F[n] be the list of parentheses at length 2n
        """
        F: List[List[s..]] = [[] ___ _ __ r..(n + 1)]
        F[0].a..("")
        ___ i __ r..(1, n+1
            ___ j __ r..(i
                ___ s1 __ F[j]:
                    ___ s2 __ F[i-j-1]:
                        F[i].a..(f"({s1}){s2}")

        r.. F[n]
