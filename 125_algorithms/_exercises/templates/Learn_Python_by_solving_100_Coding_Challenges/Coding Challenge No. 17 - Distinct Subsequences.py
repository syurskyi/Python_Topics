# Distinct Subsequence
# Question: Given a string S and a string T, count the number of distinct subsequences of T in S.
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
# Here is an example:
# S = "rabbbit", T = "rabbit"
# Return 3.
# Solutions:


c_ Solution:
    # @return an integer
    # @dp
    # dp[i][j] means how many first j of T is sub of first i of S.
    ___ numDistinct S, T:
        dp _ [[0 ___ i __ ra.. le. T+1] ___ j __ ra.. le. S+1]
        ___ j __ ra.. le. S+1:
            dp[j][0] _ 1
        ___ i __ ra.. 1, le. S+1:
            ___ j __ ra.. 1, mi. i+1, le. T+1:
                __ S[i-1] __ T[j-1]:
                    dp[i][j] _ dp[i-1][j] + dp[i-1][j-1]
                ____
                    dp[i][j] _ dp[i-1][j]
        r_ dp[le. S][le. T]


Solution.numDistinct "rabbbit","rabbit"