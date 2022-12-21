#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-04-04 17:39:46


c.. Solution o..
    # Easy to understand.  Refer to
    # https://leetcode.com/discuss/32204/simple-c-solution-8ms-13-lines
    ___ longestPalindrome  s
        __ n.. s:
            r_ ""
        s_len = l..(s)
        __ s_len __ 1:
            r_ s
        max_start, max_end = 0, 1   # Make sure s[start:end] is palindrome
        i = 0
        _____ i < s_len:
            # No need to check the remainming, pruning here
            __ max_end - max_start >= (s_len-i) * 2 - 1:
                break
            left, right = i, i+1
            # Skip duplicate characters i.
            _____ right < s_len and s[right-1] __ s[right]:
                right += 1
            i = right
            _____ left-1 >= 0 and right < s_len and s[left-1] __ s[right]:
                left -= 1
                right += 1
            __ right-left > max_end-max_start:
                max_start = left
                max_end = right
        r_ s[max_start:max_end]

"""
""
"a"
"aa"
"dcc"
"aaaa"
"cccd"
"ccccdc"
"abcdefead"
"""
