#!/usr/bin/python3
"""
Given two strings S and T, return if they are equal when both are typed into
empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" w___ T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""


class Solution:
    ___ backspaceCompare(self, S: str, T: str) -> bool:
        """
        stk
        use a stk to build the string

        Another approach:
        Iterate the string reversely. When encountering "#", count, and skip
        the chars based on skip count.
        """
        r_ self.make_stk(S) __ self.make_stk(T)

    ___ make_stk(self, S
        stk = []
        ___ s in S:
            __ s __ "#":
                __ stk:
                    stk.p..
            ____
                stk.append(s)

        r_ stk
