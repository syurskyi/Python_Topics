#!/usr/bin/python3
"""
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make
two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
possible to achieve this.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
"""


c_ Solution:
    ___ minimumDeleteSum  s1: s.., s2: s..) __ i..:
        """
        let F[i][j] be the cost to delete & make s1[:i] == s2[:j]
        F[i][j] = min
           F[i][j-1] + cost (delete s2[j-1], and then delete & make s1[:i] == s2[:j-1])
           F[i-1][j] + cost
           F[i-1][j-1] if (s1[i-1] == s2[j-1])
        """
        m, n = l..(s1), l..(s2)
        F = [[float('inf') ___ _ __ r..(n + 1)] ___ _ __ r..(m + 1)]
        F[0][0] = 0
        ___ i __ r..(1, m + 1):
            F[i][0] = F[i-1][0] + o..(s1[i-1])
        ___ j __ r..(1, n + 1):
            F[0][j] = F[0][j-1] + o..(s2[j-1])
        ___ i __ r..(1, m + 1):
            ___ j __ r..(1, n + 1):
                F[i][j] = m..(
                    F[i][j],
                    F[i][j-1] + o..(s2[j-1]),
                    F[i-1][j] + o..(s1[i-1]),
                )
                __ s1[i-1] __ s2[j-1]:
                    F[i][j] = m..(
                        F[i][j],
                        F[i-1][j-1],
                    )

        r.. F[m][n]

    ___ minimumDeleteSum_error  s1: s.., s2: s..) __ i..:
        """
        let F[i][j] be the cost to make s1[:i] == s2[:j]
        F[i][j] = min
           F[i][j-1] + cost (delete s2[j-1])
           F[i-1][j] + cost
           F[i-1][j-1] if (s1[i-1] == s2[j-1])

        Error at initial conditions
        """
        m, n = l..(s1), l..(s2)
        F = [[float('inf') ___ _ __ r..(n + 1)] ___ _ __ r..(m + 1)]
        F[0][0] = 0
        F[1][0] = o..(s1[0])
        F[0][1] = o..(s2[0])
        ___ i __ r..(1, m + 1):
            ___ j __ r..(1, n + 1):
                F[i][j] = m..(
                    F[i][j],
                    F[i][j-1] + o..(s2[j-1]),
                    F[i-1][j] + o..(s1[i-1]),
                )
                __ s1[i-1] __ s2[j-1]:
                    F[i][j] = m..(
                        F[i][j],
                        F[i-1][j-1],
                    )

        r.. F[m][n]


__ _______ __ _______
    ... Solution().minimumDeleteSum("sea", "eat") __ 231
    ... Solution().minimumDeleteSum("delete", "leet") __ 403
