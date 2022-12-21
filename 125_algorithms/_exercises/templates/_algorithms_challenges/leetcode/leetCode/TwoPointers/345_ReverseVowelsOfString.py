#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-04 12:05:02


c.. Solution o..
    ___ reverseVowels  s
        # Scan while incrementing start and decrementing end.
        all_vowels = s..(['a', 'e', 'i', 'o', 'u',
                          'A', 'E', 'I', 'O', 'U'])
        s = list(s)
        left, right = 0, l..(s) - 1
        _____ left < right:
            __ s[left] __ all_vowels a.. s[right] __ all_vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            ____ s[left] __ all_vowels:
                right -= 1
            ____ s[right] __ all_vowels:
                left += 1
            ____
                left += 1
                right -= 1
        r_ "".join(s)

"""
""
"hello"
"leetcode"
"Administrator"
"""
