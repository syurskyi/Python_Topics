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
    def wordBreak(self, s, dict):
        if len( s ) == 0 or len(dict) == 0:
            return False
        dp = [ 0 ]
        for i in range(1, len( s ) + 1):
            for j in range( len( dp ) - 1, -1, -1):
                substr = s[dp[j] : i]
                if substr in dict:
                    dp.append(i)
                    break
        return dp[-1] == len( s )


dict = ["hall", "mark"]
Solution().wordBreak("hallmark",dict)