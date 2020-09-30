# Edit Distance
# Question: Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
# (Each operation is counted as 1 step.)
# You have the following 3 operations permitted on a word:
# a) Insert a character
# b) Delete a character
# c) Replace a character
# Solutions:


class Solution:
    # @return an integer
    ___ minDistance(word1, word2):
        m=len(word1)+1; n=len(word2)+1
        dp = [[0 ___ i __ ra..(n)] ___ j __ ra..(m)]
        ___ i __ ra..(n):
            dp[0][i]=i
        ___ i __ ra..(m):
            dp[i][0]=i
        ___ i __ ra..(1,m):
            ___ j __ ra..(1,n):
                dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1))
        r_ dp[m-1][n-1]


Solution.minDistance("Freebirds", "Dinner")