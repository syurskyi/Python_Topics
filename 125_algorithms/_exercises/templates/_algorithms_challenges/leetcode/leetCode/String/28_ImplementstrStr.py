#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    # Not notoriously hard-to-understand algorithm KMP
    ___ strStr  haystack, needle
        # Return 0 if needle is ""
        __ n.. needle:
            r_ 0
        length = l..(haystack)

        # If one char in haystack is same with needle[0],
        # then verify the other chars in needle.
        ___ i __ r..(length-l..(needle)+1
            __ haystack[i:i+l..(needle)] __ needle:
                r_ i

        r_ -1

"""
""
""
"abaa"
"aa"
"aaabbb"
"abbb"
"""
