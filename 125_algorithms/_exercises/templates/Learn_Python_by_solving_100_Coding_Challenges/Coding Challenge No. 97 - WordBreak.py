# Word Break
# Question: Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# For example, given
# s = “hallmark",
# dict = [“hall", “mark"].
# Return true because " hallmark " can be segmented as " hall mark".
# Solutions:


c_ Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    ___ wordBreak(, s, di..):
        __ le.( s ) __ 0 o. le.(di..) __ 0:
            r_ F..
        dp _ [ 0 ]
        ___ i __ ra..(1, le.( s ) + 1):
            ___ j __ ra..( le.( dp ) - 1, -1, -1):
                substr _ s[dp[j] : i]
                __ substr __ di..:
                    dp.ap..(i)
                    b..
        r_ dp[-1] __ le.( s )


di.. _ ["hall", "mark"]
Solution().wordBreak("hallmark",di..)