#!/usr/bin/python3
"""
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left
or to the right.



After each second, each domino that is falling to the left pushes the adjacent
domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes
standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays
still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino
expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th
domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state.

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'
"""


c_ Solution:
    ___ pushDominoes  dominoes: s..) __ s..:
        """
        DP L & R from both ends
        Let L[i] be the distance to the "L" from the right

        we will consider that a falling domino expends no additional force
        """
        n = l..(dominoes)
        L = [float("inf") ___ i __ r..(n)]
        R = [float("inf") ___ i __ r..(n)]
        ___ i __ r..(n-1, -1, -1):
            __ dominoes[i] __ "L":
                L[i] = 0
            ____ dominoes[i] __ "R":
                L[i] = float("inf")
            ____ i + 1 < n:
                L[i] = L[i+1] + 1

        ___ i __ r..(n):
            __ dominoes[i] __ "R":
                R[i] = 0
            ____ dominoes[i] __ "L":
                R[i] = float("inf")
            ____ i - 1 >= 0:
                R[i] = R[i-1] + 1

        ret    # list
        ___ i __ r..(n):
            d = m..(R[i], L[i])
            __ d __ float("inf"):
                cur = "."
            ____ R[i] __ L[i]:
                cur = "."
            ____ d __ R[i]:
                cur = "R"
            ____:
                cur = "L"
            ret.a..(cur)

        r.. "".j..(ret)


__ _______ __ _______
    ... Solution().pushDominoes(".L.R...LR..L..") __ "LL.RR.LLRRLL.."
