#!/usr/bin/python3
"""
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so
that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation:
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
Note:

1 <= S.length = shifts.length <= 20000
0 <= shifts[i] <= 10 ^ 9
"""
____ typing _______ List


c_ Solution:
    ___ shiftingLetters(self, S: s.., shifts: List[i..]) __ s..:
        """
        preprocess shifts
        """
        n = l..(shifts)
        ___ i __ r..(n-2, -1, -1):
            shifts[i] += shifts[i+1]
            shifts[i] %= 26

        ret    # list
        ___ i, s __ e..(S):
            b = (ord(s) + shifts[i] - ord('a')) % 26 + ord('a')
            b = chr(b)
            ret.a..(b)

        r.. "".j..(ret)


__ _______ __ _______
    ... Solution().shiftingLetters("abc", [3, 5, 9]) __ "rpl"
