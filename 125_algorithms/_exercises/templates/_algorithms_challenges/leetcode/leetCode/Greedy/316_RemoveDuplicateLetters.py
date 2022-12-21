#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Refer to:
# https://leetcode.com/discuss/73777/easy-to-understand-iterative-java-solution


c.. Solution o..
    ___ removeDuplicateLetters  s
        """
        Given the string s, the greedy choice is the smallest s[i],
        s.t. the suffix s[i .. ] contains all the unique letters.
        After determining the greedy choice s[i], get a new string by:
            1. removing all letters to the left of s[i],
            2. removing all s[i] in s[i+1:].
        We then recursively solve the sub problem s'.
        """

        __ n.. s:
            r_ ""

        # 1. Find out the last appeared position for each letter;
        char_dict _ # dict
        ___ i, c __ enumerate(s
            char_dict[c] = i

        # 2. Find out the smallest index (2) from the map in step 1;
        pos = l..(s)
        ___ i __ char_dict.values(
            __ i < pos:
                pos = i

        # 3. The first letter in the final result must be
        #    the smallest letter from index 0 to index (2);
        char = s[0]
        res_pos = 0
        ___ i __ r..(1, pos+1
            __ s[i] < char:
                char = s[i]
                res_pos = i
        # 4. Find out remaining letters with the new s.
        new_s = [c ___ c __ s[res_pos+1:] __ c != char]
        r_ char + self.removeDuplicateLetters("".join(new_s))


# Use Stack to avoid recursive, more quickly.
c.. Solution_2 o..
    ___ removeDuplicateLetters  s
        char_dict _ # dict
        used _ # dict
        ___ c __ s:
            char_dict[c] = char_dict.get(c, 0) + 1
            used[c] = False

        res   # list        # Use as a Stack.
        ___ c __ s:
            char_dict[c] -= 1
            __ used[c]:
                c_

            _____ res a.. res[-1] > c a.. char_dict[res[-1]] > 0:
                used[res[-1]] = False
                res.pop()

            res.append(c)
            used[c] = True
        r_ "".join(res)

"""
""
"bcabc"
"abacb"
"cbacdcbc"
"""
