#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ isAnagram  s, t
        char_hash _ # dict
        ___ c __ s:
            char_hash[c] = char_hash.get(c, 0) + 1

        ___ c __ t:
            __ c n.. __ char_hash:
                r_ False
            char_hash[c] -= 1
            __ char_hash[c] < 0:
                r_ False
        r_ n.. s..(char_hash.values())

"""
""
""
"acd"
"ac"
"anagram"
"nagaram"
"rat"
"car"
"""
