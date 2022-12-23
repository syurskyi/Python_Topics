#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ minDistance  word1, word2
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len_w1 = l..(word1)
        len_w2 = l..(word2)

        # dp[i][j]: minimum number of steps convert word1[0,i) to word2[0,j)
        dp = [[0 ___ j __ r..(len_w2+1)] ___ i __ r..(len_w1+1)]

        # initial the dp array
        dp[0][0] = 0
        ___ j __ r..(1, len_w2+1
            dp[0][j] = j
        ___ i __ r..(1, len_w1+1
            dp[i][0] = i

        ___ i __ r..(1, len_w1+1
            ___ j __ r..(1, len_w2+1
                __ word1[i-1] __ word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                ____
                    dp[i][j] = m.. 
                        dp[i-1][j-1] + 1,
                        dp[i-1][j] + 1,
                        dp[i][j-1] + 1,)

        r_ dp[len_w1][len_w2]
