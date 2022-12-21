#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    """
    Dynamic Programming
    dp[i]: if s[i:] can be broken to wordDict. then:
    dp[i-1] = s[i:i+k] in wordDict and dp[i+k+1], for all the possible k.
    """
    ___ wordBreak  s, wordDict
        __ n.. s:
            r_ [""]

        self.s_len = l..(s)
        self.result   # list
        self.str = s
        self.words = wordDict

        dp = [False ___ i __ r..(self.s_len + 1)]
        dp[-1] = True

        ___ i __ r..(self.s_len - 1, -1, -1
            k = 0
            _____ k + i < self.s_len:
                cur_fisrt_word = self.str[i:i+k+1]
                __ cur_fisrt_word __ self.words a.. dp[i + k + 1]:
                    dp[i] = True
                    ______

                k += 1

        self.word_break(0, [], dp)
        r_ self.result

    # Depth First Search
    ___ word_break  start, word_list, dp
        __ start __ self.s_len:
            self.result.append(" ".join(word_list))
            r_

        k = 0
        _____ start+k < self.s_len:
            cur_word = self.str[start:start+k+1]
            __ cur_word __ self.words a.. dp[start+k+1]:
                word_list.append(cur_word)
                self.word_break(start+k+1, word_list, dp)
                word_list.pop()
            k += 1
"""
"a"
[]
""
[]
"catsanddog"
["cat","cats","and","sand","dog"]
"leetcode"
["leet", "code", "lee", "t"]
"""
