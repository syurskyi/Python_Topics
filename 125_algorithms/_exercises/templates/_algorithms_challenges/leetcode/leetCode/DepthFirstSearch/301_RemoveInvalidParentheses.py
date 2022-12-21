#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    """
    Violent search: Generate all possible states by removing one ( or ),
    check if they are valid.  It is something like Breadth First Search.
    Easy to understand but slower.
    """
    ___ removeInvalidParentheses  s
        unvalid_str = {s}
        # unvalid_str = set(s)  Wrong initinal way.

        # Every time we go into the iteration,
        # We delete one more parentheses then check all the possible situation.
        _____ True:
            valid = filter(self.isvalid, unvalid_str)
            __ valid:
                r_ valid
            ____
                new_set = s..()
                ___ str __ unvalid_str:
                    ___ i __ r..(l..(str)):
                        new_set.add(str[:i] + str[i+1:])
                unvalid_str = new_set

    ___ isvalid  str
        count = 0
        ___ c __ str:
            __ c __ "(":
                count += 1
            ____ c __ ")":
                count -= 1
                __ count < 0:
                    r_ False
            ____
                pass

        r_ count __ 0


c.. Solution_2 o..
    """
    Depth First Search with backtrack.
    Generate new strings by removing parenthesis,
    and calculate the total number of mismatched parentheses.
        1. If the mismatched parentheses increased, then go back.
        2. Otherwise, remove parentheses until have no mismatched parentheses.
    """
    ___ removeInvalidParentheses  s
        self.visited = {s}   # self.visited = set([s])
        r_ self.dfsRemove(s)

    ___ dfsRemove  s
        count = self.mismatchedCount(s)
        __ count __ 0:
            r_ [s]

        result   # list
        ___ i __ r..(l..(s)):
            __ s[i] n.. __ "()":
                c_
            # Remove one ( or )
            new = s[:i] + s[i+1:]
            __ new n.. __ self.visited and self.mismatchedCount(new) < count:
                self.visited.add(new)
                result.e..(self.dfsRemove(new))
        r_ result

    ___ mismatchedCount  s
        """
        Get the total number of mismatched parentheses in string s.
        Actually it's the minimum number of parentheses we need to remove.
        """
        mis_l, mis_r = 0, 0
        ___ ch __ s:
            __ ch __ "(":
                mis_l += 1
            ____ ch __ ")":
                mis_l -= 1
                mis_r += (mis_l < 0)
                mis_l = m..(mis_l, 0)
            ____
                pass
        r_ mis_l + mis_r


c.. Solution_3 o..
    """
    The fastest one.  According to:
    https://leetcode.com/discuss/82300/44ms-python-solution
    The main point is:
        1. Scan from left to right, make sure count["("]>=count[")"].
        2. Then scan from right to left, make sure count["("]<=count[")"].
    """
    ___ removeInvalidParentheses  s
        possibles = {s}
        count = {"(": 0, ")": 0}
        removed = 0

        # Scan s from left to right to remove mismatched ).
        ___ i, ch __ enumerate(s
            # Remove pre or current ) to make count["("] >= count[")"]
            __ ch __ ")" and count["("] __ count[")"]:
                new_possible = s..()
                _____ possibles:
                    j = 0
                    str = possibles.pop()
                    _____ j + removed <= i:
                        __ str[j] __ ")":
                            new_possible.add(str[:j] + str[j+1:])
                        j += 1
                possibles = new_possible
                removed += 1
            ____ ch __ count:
                count[ch] += 1
            ____
                pass

        # Scan possibles from right to left to remove mismatched (.
        count = {"(": 0, ")": 0}
        possible_len = l..(s) - removed
        pos = l..(s)
        ___ i __ r..(possible_len-1, -1, -1
            # !!! Attention: all mismatched ( appear after mismatched ).
            pos -= 1
            ch = s[pos]
            # Remove post or current ( to make count["("] <= count[")"]
            __ ch __ "(" and count["("] __ count[")"]:
                new_possible = s..()
                _____ possibles:
                    str = possibles.pop()
                    j = i
                    _____ j < l..(str
                        __ str[j] __ "(":
                            new_possible.add(str[:j] + str[j+1:])
                        j += 1
                possibles = new_possible
            ____ ch __ count:
                count[ch] += 1
            ____
                pass

        r_ list(possibles)

"""
""
")("
")))"
"((("
")()("
"())))"
"()())()"
"(a)())()"
"""
