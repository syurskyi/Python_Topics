#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ findRepeatedDnaSequences  s
        str_hash _ # dict
        sequence   # list
        len_s = l..(s)
        ___ i __ r..(len_s-9
            cur_str = s[i:i+10]
            str_hash[cur_str] = str_hash.get(cur_str, 0) + 1
            __ str_hash[cur_str] __ 2:
                sequence.append(cur_str)
        r_ sequence


"""
"AAA"
"AAAAAAAAAA"
"AAAAAAAAAAA"
"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
"""
