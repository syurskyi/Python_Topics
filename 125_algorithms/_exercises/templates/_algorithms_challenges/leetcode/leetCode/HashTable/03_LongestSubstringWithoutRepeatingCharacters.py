#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ lengthOfLongestSubstring  s
        """
        :type s: str
        :rtype: int
        """

        max_length = 0
        start = 0   # Start index of the substring without repeating characters
        end = 0     # End index of the substring without repeating characters
        char_dict _ # dict

        ___ index __ r..(l..(s)):
            char = s[index]
            # Find out a repeating character. So reset start and end.
            __ char __ char_dict and start <= char_dict[char] <= end:
                start = char_dict[char] + 1
                end = index
            # char is not in the substring already, add it to the substring.
            ____
                end = index
                __ end - start + 1 > max_length:
                    max_length = end - start + 1
            char_dict[char] = index

        r_ max_length

"""
""
"bbbbb"
"abcabcbb"
"""
