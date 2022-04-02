"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only
once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""
__author__ = 'Daniel'


c_ Solution(o..
    ___ removeDuplicateLetters  s
        """
        :type s: str
        :rtype: str
        """
        last_pos = [-1 ___ _ __ x..(26)]
        n = l..(s)
        ___ i __ x..(n-1, -1, -1
            __ last_pos[_idx(s[i])] __ -1:
                last_pos[_idx(s[i])] = i

        stk    # list
        stk_set = s..()
        ___ i __ x..(n
            v = s[i]
            __ v n.. __ stk_set:
                w.... stk a.. stk[-1] > v a.. last_pos[_idx(stk[-1])] > i:
                    p = stk.pop()
                    stk_set.remove(p)
                stk.a..(v)
                stk_set.add(v)

        r.. "".j..(stk)

    ___ _idx  x
        r.. o..(x) - o..('a')


__ _______ __ _______
    ... Solution().removeDuplicateLetters("cbacdcbc") __ "acdb"