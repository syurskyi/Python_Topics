#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ minWindow  s, t
        s_size = l..(s)
        __ n.. t or n.. s:
            r_ ""

        # Keep the present tims of all characters in T.
        t_dict _ # dict
        ___ char __ t:
            __ char n.. __ t_dict:
                t_dict[char] = 1
            ____
                t_dict[char] += 1

        count = 0
        t_size = l..(t)
        start = end = 0
        # min_window(start, end): the suitable window's left and right board
        min_window = (0, s_size)
        # Keep the present tims of the window's characters that appear in T.
        win_dict _ # dict
        _____ end < s_size:
            cur_char = s[end]
            __ cur_char __ t_dict:
                __ cur_char n.. __ win_dict:
                    win_dict[cur_char] = 1
                ____
                    win_dict[cur_char] += 1
                __ win_dict[cur_char] <= t_dict[cur_char]:
                    count += 1

            __ count __ t_size:
                # Move start toward to cut the window's size.
                is_suitable_window = True
                _____ start <= end a.. is_suitable_window:
                    start_char = s[start]
                    __ start_char n.. __ t_dict:
                        start += 1
                    ____
                        __ win_dict[start_char] > t_dict[start_char]:
                            win_dict[start_char] -= 1
                            start += 1
                        ____
                            is_suitable_window = False

                # Update the minimum window
                window_size = end - start + 1
                min_size = min_window[1] - min_window[0] + 1
                __ window_size < min_size:
                    min_window = (start, end)

                # Move start toward to find another suitable window
                win_dict[s[start]] -= 1
                start += 1
                count -= 1

            end += 1
        # No suitable window
        __ min_window[1] __ s_size:
            r_ ""
        r_ s[min_window[0]: min_window[1] + 1]

"""
"a"
""
"ADOBECODEBANC"
"ABCC"
"""
