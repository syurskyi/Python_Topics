#!/usr/bin/python3
"""
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that
row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a
binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.
"""
____ t___ _______ List


c_ Solution:
    ___ matrixScore  A: List[List[i..]]) __ i..:
        """
        MSB > sum of remaining digit
        => Toggle rows to set MSB to 1
        Then we cannot toggle row anymore
        Toggle the col if #0's < #1's
        """
        m, n = l..(A), l..(A[0])
        ret = 0
        ret += (1 << (n-1)) * m  # all rows with MSB being 1
        ___ j __ r..(1, n
            cnt = 0
            ___ i __ r..(m
                __ A[i][j] __ A[i][0]:
                    cnt += 1  #  number of 1's

            # toggle 
            cnt = m..(cnt, m-cnt)
            ret += (1 << (n-1-j)) * cnt

        r.. ret
