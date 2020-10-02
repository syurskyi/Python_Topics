# Decode Ways
# Question: A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# For example:
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
# The number of ways decoding "12" is 2.
# Solutions:


c_ Solution:
    # @param s is a string
    # @return an integer
    ___ numDecodings s:
        __ s__"" o. s[0]__'0': r_ 0
        dp_[1,1]
        ___ i __ ra.. 2,le. s+1:
            __ 10 <_int s[i-2:i] <_26 an. s[i-1]!_'0':
                dp.ap.. dp[i-1]+dp[i-2]
            ____ in. s[i-2:i]__10 o. in. s[i-2:i]__20:
                dp.ap.. dp[i-2]
            ____ s[i-1]!_'0':
                dp.ap.. dp[i-1]
            ____
                r_ 0
        r_ dp[le. s]

Solution.numDecodings "12"