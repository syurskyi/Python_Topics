# Palindrome Partitioning II
# Question: Given a string s, partition s such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of s.
# For example: given s = "aab", Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
# Solutions:


c_ Solution:
    # @param s, a string
    # @return an integer

    ___ partitionII(self, s):
        n _ le.(s)
        f _   # list
        p _ [[F.. ___ x __ ra..(n)] ___ x __ ra..(n)]
        #the worst case is cutting by each char
        ___ i __ ra..(n+1):
            f.ap..(n - 1 - i) # the last one, f[n]=-1
        ___ i __ reversed(ra..(n)):
            ___ j __ ra..(i, n):
                __ (s[i] __ s[j] an. (j - i < 2 o. p[i + 1][j - 1])):
                    p[i][j] _ T..
                    f[i] _ mi.(f[i], f[j + 1] + 1)
        r_ f[0]


Solution().partitionII("aab")