#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ wordBreak  s, wordDict
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        __ n.. s:
            r_ True
        __ n.. wordDict:
            r_ False
        s_len = l..(s)
        dp = [False ___ i __ r..(s_len+1)]
        dp[-1] = True
        ___ i __ r..(s_len-1, -1, -1
            k = 0
            _____ k+i < s_len:
                cur_fisrt_word = s[i:i+k+1]
                __ cur_fisrt_word __ wordDict a.. dp[i+k+1]:
                    dp[i] = True
                    ______
                ____
                    k += 1
        r_ dp[0]

"""
"leetcode"
["leet","code"]
"leetcodecode"
["leet","code"]
"""
