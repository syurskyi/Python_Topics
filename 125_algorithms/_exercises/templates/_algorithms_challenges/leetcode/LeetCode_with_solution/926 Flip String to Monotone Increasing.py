#!/usr/bin/python3
"""
A string of '0's and '1's is monotone increasing if it consists of some number
of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a
'1' to a '0'.

Return the minimum number of flips to make S monotone increasing.



Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.


Note:

1 <= S.length <= 20000
S only consists of '0' and '1' characters.
"""


c_ Solution:
    ___ minFlipsMonoIncr(self, S: s..) -> int:
        """
        let S[i] be the flipping point, leftside 0, rightside 1
        count number of 1 from the left,
        count number of 0 from the right
        O(N)
        """
        n = l..(S)
        Z = [0 ___ _ __ r..(n+1)]  # let Z[i] be #zero in A[i:]
        O = [0 ___ _ __ r..(n+1)]  # let O[i] be #one in A[:i]
        ___ i __ r..(1, n+1):
            O[i] = O[i-1]
            __ S[i-1] __ "1":
                O[i] += 1

        ___ i __ r..(n-1, -1, -1):
            Z[i] = Z[i+1]
            __ S[i] __ "0":
                Z[i] += 1

        ret = float('inf')
        ___ i __ r..(n):
            ret = m..(ret, O[i] + Z[i+1])

        r.. ret
