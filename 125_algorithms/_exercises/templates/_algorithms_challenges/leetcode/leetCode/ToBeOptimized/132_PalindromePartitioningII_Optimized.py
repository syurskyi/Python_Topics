#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Refer to: https://leetcode.com/discuss/9476/solution-does-not-need-table-palindrome-right-uses-only-space
# A better solution


c.. Solution o..
    """
    Dynamic Programming:
    """
    ___ minCut  s
        s_len = l..(s)
        # number of minnum cuts for the pre i characters
        min_cuts = [i-1 ___ i __ r..(s_len+1)]

        ___ i __ r..(s_len
            # odd length palindrome
            j = 0
            _____ i-j >= 0 a.. i+j < s_len:
                __ s[i-j] __ s[i+j]:
                    min_cuts[i+j+1] = m.. min_cuts[i+j+1], min_cuts[i-j]+1)
                    j += 1
                ____
                    ______
            # even length palindrome
            j = 1
            _____ i-j+1 >= 0 a.. i+j < s_len:
                __ s[i-j+1] __ s[i+j]:
                    min_cuts[i+j+1] = m.. min_cuts[i+j+1], min_cuts[i-j+1]+1)
                    j += 1
                ____
                    ______

        r_ min_cuts[s_len]

"""
if __name__ == "__main__":
    sol = Solution()
    print sol.minCut("aab")
    print sol.minCut("aabb")
    print sol.minCut("aabaa")
    print sol.minCut("acbca")
    print sol.minCut("acbbca")
"""
