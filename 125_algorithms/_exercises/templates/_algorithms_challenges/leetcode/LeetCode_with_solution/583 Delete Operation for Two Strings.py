#!/usr/bin/python3
"""
Given two words word1 and word2, find the minimum number of steps required to
make word1 and word2 the same, where in each step you can delete one character
in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""
____ c.. _______ d..


c_ Solution:
    ___ minDistance  word1: s.., word2: s..) __ i..:
        """
        Longest Common Subsequence (LCS)
        Find the LCS, and delete the char in BOTH strings into LCS

        Let F[i][j] be length of LCS word1[:i] and word2[:j]

        F[i][j] = F[i-1][j-1] + 1 if word1[i-1] == word2[j-1]
        F[i][j] = max(F[i-1][j], F[i][j-1])
        """
        F = d..(l....: d..(i..))
        m = l..(word1)
        n = l..(word2)

        ___ i __ r..(1, m + 1
            ___ j __ r..(1, n + 1
                __ word1[i-1] __ word2[j-1]:
                    F[i][j] = F[i-1][j-1] + 1
                ____:
                    F[i][j] = m..(
                        F[i-1][j],
                        F[i][j-1],
                    )

        r.. m - F[m][n] + n - F[m][n]

    ___ minDistance_edit_distance  word1: s.., word2: s..) __ i..:
        """
        Edit distance

        Let F[i][j] be # operations to make same for word1[:i] and word2[:j]

        F[i][j] = F[i-1][j-1] if word1[i-1] == word2[j-1]
        F[i][j] = min(F[i-1][j] + 1, F[i][j-1] + 1)
        """
        F = d..(l....: d..(i..))
        m = l..(word1)
        n = l..(word2)

        # initialization is important
        ___ i __ r..(1, m + 1
            F[i][0] = i
        ___ j __ r..(1, n + 1
            F[0][j] = j

        ___ i __ r..(1, m + 1
            ___ j __ r..(1, n + 1
                __ word1[i-1] __ word2[j-1]:
                    F[i][j] = F[i-1][j-1]
                ____:
                    F[i][j] = m..(
                        F[i-1][j] + 1,
                        F[i][j-1] + 1,
                    )

        r.. F[m][n]


__ _______ __ _______
    ... Solution().minDistance("sea", "eat") __ 2
