#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ isScramble  s1, s2
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        __ (l..(s1) != l..(s2)) or n.. l..(s1) or n.. l..(s2
            r_ False

        __ s1 __ s2:
            r_ True

        str_l = l..(s1)
        # dp[l][i][j]: whether s1[i:i+l+1] is a scrambled string of s2[j:j+l+1]
        dp = [[[False ___ i __ xrange(str_l)]
               ___ j __ xrange(str_l)] ___ l __ xrange(str_l)]

        # Initialization: dp[0][i][j], s1[i] is a scrambled string of s2[j]
        ___ i __ xrange(str_l
            ___ j __ xrange(str_l
                dp[0][i][j] = True __ s1[i] __ s2[j] else False

        ___ l __ xrange(1, str_l
            # The length of current substring is l+1
            ___ i __ xrange(str_l-l
                ___ j __ xrange(str_l-l
                    # Split the l+1 string into two parts,
                    # k is the length of first part, so 1 <= k <= l;
                    ___ k __ r..(1, l+1
                        scramble_1 = dp[k-1][i][j] and dp[l-k][k+i][k+j]
                        scramble_2 = dp[k-1][i][j+l-k+1] and dp[l-k][i+k][j]
                        dp[l][i][j] = (scramble_1 or scramble_2)
                        __ dp[l][i][j]:
                            break
        r_ dp[str_l-1][0][0]

"""
"great"
"rgeta"
"great"
"rgtae"
"""

# Implement with recursion
"""
class Solution(object):
    def isScramble(self, s1, s2):
        if (len(s1) != len(s2)) or not len(s1) or not len(s2):
            return False

        if sorted(s1) != sorted(s2):
            return False

        if s1 == s2:
            return True

        length = len(s1)
        for i in range(1, length):
            if (self.isScramble(s1[:i],s2[:i])
                and self.isScramble(s1[i:],s2[i:])):
                return True
            if (self.isScramble(s1[:i],s2[length-i:])
                and self.isScramble(s1[i:],s2[:length-i])):
                return True
        return False
"""
