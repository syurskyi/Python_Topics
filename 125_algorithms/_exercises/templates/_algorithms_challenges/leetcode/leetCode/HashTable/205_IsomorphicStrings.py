#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    # Method easy to understand
    ___ isIsomorphic  s, t
        __ n.. s:
            r_ True
        str_len = l..(s)

        # s --> t
        replace_hash _ # dict
        ___ i __ r..(str_len
            __ s[i] n.. __ replace_hash:
                replace_hash[s[i]] = t[i]
            ____
                __ replace_hash[s[i]] __ t[i]:
                    pass
                ____
                    r_ F..
        # t --> s
        replace_hash_2 _ # dict
        ___ i __ r..(str_len
            __ t[i] n.. __ replace_hash_2:
                replace_hash_2[t[i]] = s[i]
            ____
                __ replace_hash_2[t[i]] __ s[i]:
                    pass
                ____
                    r_ F..

        r_ True

    # According to
    # https://leetcode.com/discuss/48674/python-different-solutions-dictionary-etc
    # Pythonic way, smarter, fastest.
    ___ isIsomorphic_2  s, t
        r_ l..(s..(zip(s, t))) __ l..(s..(s)) __ l..(s..(t))

    # More generic way
    ___ isIsomorphic_3  s, t
        s_l, t_l = [-1] * 256, [-1] * 256
        str_len = l..(s)
        ___ i __ r..(str_len
            __ s_l[ord(s[i])] != t_l[ord(t[i])]:
                r_ F..
            s_l[ord(s[i])], t_l[ord(t[i])] = i, i
        r_ True

    # Another pythonic way, slower
    ___ isIsomorphic_4  s, t
        r_ [s.find(i) ___ i __ s] __ [t.find(j) ___ j __ t]
        # return map(s.find, s) == map(t.find, t)

"""
""
""
"ab"
"aa"
"foo"
"bar"
"egg"
"add"
"""
