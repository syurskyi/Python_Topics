"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the
 characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of
 "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""
__author__ = 'Danyang'
c_ Solution:
    ___ numDistinct  S, T):
        """
        Algorithm: dp, sub-sequence and matching

        Let W(i, j) stand for the number of subsequences of S(0, i) in T(0, j).
        If S.charAt(i) == T.charAt(j), W(i, j) = W(i-1, j-1) + W(i-1,j); Otherwise, W(i, j) = W(i-1,j).
        reference: http://www.programcreek.com/2013/01/leetcode-distinct-subsequences-total-java/

          - r a b b b i t
        - 1 1 1 1 1 1 1 1
        r 0 1 1 1 1 1 1 1
        a 0 0 1 1 1 1 1 1
        b 0 0 0 1 2 3 3 3
        b 0 0 0 0 1 3 3 3
        i 0 0 0 0 0 0 3 3
        t 0 0 0 0 0 0 0 3


        Thought:
        (in this case, S as the vertical line, T as the horizontal line
        f[i][j] is the number of distant subsequences of T[:j] in S[:i]
        f[i][j] is at least f[i-1][j]
        if S[i]==T[j]:
        transit from f[i-1][j-1] (if you delete both S[i] and T[j])
        f[i][j] += f[i-1][j-1]

        :param S: string
        :param T: string
        :return: integer
        """
        len_s = l..(S)
        len_t = l..(T)

        dp = [[-1 ___ _ __ x..(len_s+1)] ___ _ __ x..(len_t+1)]
        ___ col __ x..(len_s+1):
            dp[0][col] = 1
        ___ row __ x..(1, len_t+1):
            dp[row][0] = 0

        ___ row __ x..(1, len_t+1):
            ___ col __ x..(1, len_s+1):
                __ S[col-1]__T[row-1]:
                    dp[row][col] = dp[row][col-1]+dp[row-1][col-1]
                ____:
                    dp[row][col] = dp[row][col-1]

        r.. dp[-1][-1]

__ _____ __ ____
    ... Solution().numDistinct("rabbbit", "rabbit")__3