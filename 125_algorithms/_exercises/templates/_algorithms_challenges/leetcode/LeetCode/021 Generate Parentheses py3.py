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
from typing ______ List


class Solution:
    ___ generateParenthesis(self, n: int) -> List[str]:
        """
        Method 1 - backtracking
        Method 2 - dp
        Let F[n] be the list of parentheses at length 2n
        """
        F: List[List[str]] = [[] ___ _ __ range(n + 1)]
        F[0].append("")
        ___ i __ range(1, n+1
            ___ j __ range(i
                ___ s1 __ F[j]:
                    ___ s2 __ F[i-j-1]:
                        F[i].append(f"({s1}){s2}")

        r_ F[n]
