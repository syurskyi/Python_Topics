c_ Solution o..
    #https://discuss.leetcode.com/topic/20094/my-c-solutions-recursion-with-cache-dp-recursion-with-cache-and-pruning-with-explanation-4ms/2
    # def isScramble(self, s1, s2):
    #     """
    #     :type s1: str
    #     :type s2: str
    #     :rtype: bool
    #     """
    #     # recursive
    #     if s1 == s2:
    #         return True
    #     if len(s1) != len(s2):
    #         return False
    #     ls = len(s1)
    #     letters = [0] * 26
    #     for i in range(ls):
    #         letters[ord(s1[i]) - ord('a')] += 1
    #         letters[ord(s2[i]) - ord('a')] -= 1
    #     for i in range(26):
    #         if letters[i] != 0:
    #             return False
    #     for i in range(1, ls):
    #         if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]):
    #             return True
    #         if self.isScramble(s1[0:i], s2[ls - i:]) and self.isScramble(s1[i:], s2[:ls - i]):
    #             return True
    #     return False

    ___ isScramble  s1, s2, memo={}
        # recursive with memo
        # Check with sorted is fundamental, otherwise TLE
        __ l.. s1) != l.. s2) or s..(s1) != s..(s2
            r_ F..
        __ l.. s1) <= l.. s2) <= 1:
            r_ s1 __ s2
        __ s1 __ s2:
            r_ T..
        __ (s1, s2) __ memo:
            r_ memo[s1, s2]
        n = l.. s1)
        ___ i __ r.. 1, n
            a = isScramble(s1[:i], s2[:i], memo) and isScramble(s1[i:], s2[i:], memo)
            __ n.. a:
                b = isScramble(s1[:i], s2[-i:], memo) and isScramble(s1[i:], s2[:-i], memo)
            __ a or b:
                memo[s1, s2] = T..
                r_ T..
        memo[s1, s2] = F..
        r_ F..

    # def isScramble(self, s1, s2):
    #     # dp TLE
    #     if s1 == s2:
    #         return True
    #     if len(s1) != len(s2):
    #         return False
    #     ls = len(s1)
    #     letters = [0] * 26
    #     for i in range(ls):
    #         letters[ord(s1[i]) - ord('a')] += 1
    #         letters[ord(s2[i]) - ord('a')] -= 1
    #     for i in range(26):
    #         if letters[i] != 0:
    #             return False
    #     dp = [[[False] * ls for i in range(ls)] for i in range(ls + 1)]
    #     for i in range(ls):
    #         for j in range(ls):
    #             dp[1][i][j] = (s1[i] == s2[j])
    #
    #     for cur_len in range(2, ls + 1):
    #         for i in range(ls - cur_len + 1):
    #             for j in range(ls - cur_len + 1):
    #                 dp[cur_len][i][j] = False
    #                 for k in range(1, cur_len):
    #                     if dp[cur_len][i][j]:
    #                         break
    #                     dp[cur_len][i][j] = dp[cur_len][i][j] or (dp[k][i][j] and dp[cur_len - k][i + k][j + k])
    #                     dp[cur_len][i][j] = dp[cur_len][i][j] or (dp[k][i + cur_len - k][j] and dp[cur_len - k][i][j + k])
    #     return dp[ls][0][0]


