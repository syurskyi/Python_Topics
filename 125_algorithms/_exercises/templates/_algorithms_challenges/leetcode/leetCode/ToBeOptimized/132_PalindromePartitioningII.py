#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    """
    Dynamic Programming:
    cuts[i]: minimum cuts needed for a palindrome partitioning of s[i:]
    is_palindrome[i][j]: whether s[i:i+1] is palindrome
    """
    ___ minCut  s
        __ n.. s:
            r_ 0
        s_len = l..(s)

        is_palindrome = [[False ___ i __ r..(s_len)]
                         ___ j __ r..(s_len)]

        cuts = [s_len-1-i ___ i __ r..(s_len)]
        ___ i __ r..(s_len-1, -1, -1
            ___ j __ r..(i, s_len
                # if self.is_palindrome(i, j):
                __ ((j-i < 2 and s[i] __ s[j]) or
                        (s[i] __ s[j] and is_palindrome[i+1][j-1])):
                    is_palindrome[i][j] = True
                    __ j __ s_len - 1:
                        cuts[i] = 0
                    ____
                        cuts[i] = min(cuts[i], 1+cuts[j+1])
                ____
                    pass

        r_ cuts[0]

"""
if __name__ == "__main__":
    sol = Solution()
    print sol.minCut("aab")
    print sol.minCut("aabb")
    print sol.minCut("aabaa")
    print sol.minCut("acbca")
    print sol.minCut("acbbca")
"""
