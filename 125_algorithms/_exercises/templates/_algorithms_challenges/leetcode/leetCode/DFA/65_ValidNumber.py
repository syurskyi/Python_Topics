#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ isNumber  s
        """DFA

        Details can be found here:
        https://github.com/xuelangZF/LeetCode/blob/master/Images/65_ValidNumber.png
        https://github.com/xuelangZF/LeetCode/blob/master/Images/65_StateConvert.png
        """
        s = s.strip()
        __ n.. s:
            r_ False

        # DFA states change table
        DFA_states_change = {
            0: {1: 2, 2: 1, 3: 8, 4: -1},
            1: {1: 2, 2: -1, 3: 8, 4: -1},
            2: {1: 2, 2: -1, 3: 3, 4: 5},
            3: {1: 4, 2: -1, 3: -1, 4: 5},
            4: {1: 4, 2: -1, 3: -1, 4: 5},
            5: {1: 7, 2: 6, 3: -1, 4: -1},
            6: {1: 7, 2: -1, 3: -1, 4: -1},
            7: {1: 7, 2: -1, 3: -1, 4: -1},
            8: {1: 4, 2: -1, 3: -1, 4: -1}
        }
        current_state = 0
        ___ char __ s:
            input_num = self.input_num(char)
            __ n.. input_num:
                r_ False
            next_state = DFA_states_change[current_state][input_num]
            __ next_state __ -1:
                r_ False
            current_state = next_state

        __ (current_state __ 2 or current_state __ 3 or
           current_state __ 4 or current_state __ 7
            r_ True
        ____
            r_ False

    ___ input_num  char
        __ char __ "0123456789":
            r_ 1
        ____ char __ "+-":
            r_ 2
        ____ char __ ".":
            r_ 3
        ____ char __ "e":
            r_ 4
        ____
            r_ 0

# True
"""
" .1"
"012"
"+12"
"-12"
"12e1"
"12e-1"
"12e+1"
"12e0"
"0e1"
"-1e1"
"1.2"
".2"
".1e1"
"+.2"
"1."
"      .1 "
"46.e3"
"""

# False
"""
""
".e1"
"+.e3"
"10e1.2"
"+-12"
"12e"
"e1"
"1e1e1"
"0xaf"
"      .1 2"
"."
"  ."
" -."
"""
