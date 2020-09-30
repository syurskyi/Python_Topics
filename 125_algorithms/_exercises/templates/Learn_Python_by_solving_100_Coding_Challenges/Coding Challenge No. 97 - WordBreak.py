# Word Break
# Question: Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# For example, given
# s = “hallmark",
# dict = [“hall", “mark"].
# Return true because " hallmark " can be segmented as " hall mark".
# Solutions:


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    ___ wordBreak(self, s, dict):
        if len( s ) == 0 or len(dict) == 0:
            r_ False
        dp = [ 0 ]
        ___ i __ ra..(1, len( s ) + 1):
            ___ j __ ra..( len( dp ) - 1, -1, -1):
                substr = s[dp[j] : i]
                if substr __ dict:
                    dp.append(i)
                    break
        r_ dp[-1] == len( s )


dict = ["hall", "mark"]
Solution().wordBreak("hallmark",dict)