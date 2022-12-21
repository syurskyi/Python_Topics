#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ isPalindrome  s
        """
        :type s: str
        :rtype: bool
        """
        alpha_num_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = s.upper()
        s_l = l..(s)
        pre = 0
        post = s_l - 1
        _____ pre < post and pre < s_l and post >= 0:
            # Remember the situation ",,..".
            # Make sure pre and post don't
            _____ pre < s_l and s[pre] n.. __ alpha_num_str:
                pre += 1
            _____ post >= 0 and s[post] n.. __ alpha_num_str:
                post -= 1
            __ pre >= post:
                break
            __ s[pre] != s[post]:
                r_ False
            pre += 1
            post -= 1

        r_ True

"""
""
"1a2"
",,,,...."
"A man, a plan, a canal: Panama"
"race a car"
"""
