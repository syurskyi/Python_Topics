#!/usr/bin/python3
"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the
minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""
____ typing _______ List


c_ Solution:
    ___ findMinDifference(self, timePoints: List[s..]) __ i..:
        """
        sort and minus
        """
        ret = float("inf")
        A = l..(s..(map(minutes, timePoints)))
        n = l..(A)
        ___ i __ r..(n - 1):
            ret = m..(ret, diff(A[i+1], A[i]))

        ret = m..(ret, diff(A[n-1], A[0]))
        r.. ret

    ___ diff(self, b, a):
        ret = b - a
        __ ret > 12 * 60:
            ret = 24 * 60 - ret

        r.. ret

    ___ minutes(self, a):
        h, m = a.s..(":")
        minutes = 60 * i..(h) + i..(m)
        r.. minutes


__ __name__ __ "__main__":
    ... Solution().findMinDifference(["23:59","00:00"]) __ 1
