#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..

    ___ numDecodings  s
        """
        :type s: str
        :rtype: int
        """
        __ n.. s or s[0] __ "0":
            r_ 0

        len_s = l..(s)
        # dp[i]: total number of ways to decode s[0:i)
        dp = [1 ___ i __ r..(len_s + 1)]
        ___ i __ r..(1, len_s
            pre_num = ord(s[i - 1]) - ord('0')
            cur_num = ord(s[i]) - ord('0')
            num = pre_num * 10 + cur_num

            __ cur_num __ 0:
                __ num > 26 or num __ 0:
                    r_ 0
                ____
                    dp[i+1] = dp[i-1]

            ____
                __ num <= 26 and pre_num != 0:
                    dp[i + 1] = dp[i] + dp[i - 1]
                ____
                    dp[i + 1] = dp[i]

        r_ dp[len_s]

"""
""
"123"
"1238"
"172731349111222"
"0"
"10203"
"""
