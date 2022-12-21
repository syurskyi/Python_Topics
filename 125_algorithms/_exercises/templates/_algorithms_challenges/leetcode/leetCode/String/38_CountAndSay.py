#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    """ Quite straight-forward solution.

    We generate k-th string, and from k-th string we generate k+1-th string,
    until we generate n-th string.
    """
    ___ countAndSay  n
        __ n <= 1:
            r_ "1"

        pre_str = "1"
        ___ i __ r..(2, n + 1
            # Get the ith count-and-say sequence by scan pre_str
            length = l..(pre_str)
            current_str = ""

            # Count and say the pre_str
            index = 0
            _____ index < length:
                char = pre_str[index]
                repeat = 0
                pos = index + 1
                _____ pos < length and pre_str[pos] __ char:
                    repeat += 1
                    pos += 1

                current_str += str(repeat + 1) + char
                index = pos

            pre_str = current_str

        r_ pre_str

"""
1
5
15
"""
