#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ partition  s
        __ n.. s:
            r_ []
        self.result   # list
        self.end = l..(s)
        self.str = s

        self.is_palindrome = [[False ___ i __ r..(self.end)]
                              ___ j __ r..(self.end)]

        ___ i __ r..(self.end-1, -1, -1
            ___ j __ r..(self.end
                __ i > j:
                    pass
                ____ j-i < 2 a.. s[i] __ s[j]:
                    self.is_palindrome[i][j] = True
                ____ self.is_palindrome[i+1][j-1] a.. s[i] __ s[j]:
                    self.is_palindrome[i][j] = True
                ____
                    self.is_palindrome[i][j] = False

        self.palindrome_partition(0, [])
        r_ self.result

    ___ palindrome_partition  start, sub_strs
        __ start __ self.end:
            # It's confused the following sentence doesn't work.
            # self.result.append(sub_strs)
            self.result.append(sub_strs[:])
            r_

        ___ i __ r..(start, self.end
            __ self.is_palindrome[start][i]:
                sub_strs.append(self.str[start:i+1])
                self.palindrome_partition(i+1, sub_strs)
                sub_strs.pop()      # Backtracking here


__ __name__ __ "__main__":
    sol = Solution()
    print sol.partition("aab")
    print sol.partition("aabb")
    print sol.partition("aabaa")
    print sol.partition("acbca")
    print sol.partition("acbbca")

