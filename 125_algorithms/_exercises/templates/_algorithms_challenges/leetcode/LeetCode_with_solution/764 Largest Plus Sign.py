#!/usr/bin/python3
"""
In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those
cells in the given list mines which are 0. What is the largest axis-aligned plus
sign of 1s contained in the grid? Return the order of the plus sign. If there is
none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1
along with 4 arms of length k-1 going up, down, left, and right, and made of 1s.
This is demonstrated in the diagrams below. Note that there could be 0s or 1s
beyond the arms of the plus sign, only the relevant area of the plus sign is
checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is
marked in bold.
Example 2:

Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.
Example 3:

Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.
Note:

N will be an integer in the range [1, 500].
mines will have length at most 5000.
mines[i] will be length 2 and consist of integers in the range [0, N-1].
(Additionally, programs submitted in C, C++, or C# will be judged with a
slightly smaller time limit.)
"""
____ typing _______ List


class Solution:
    ___ orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        """
        < ^ > V four directions
        Let F[i][j][k] be the number of consecutive 1 including G[i][j] it self
        """
        G = [[1 ___ _ __ r..(N)] ___ _ __ r..(N)]
        ___ i, j __ mines:
            G[i][j] = 0

        F = [[[G[i][j] ___ _ __ r..(4)] ___ j __ r..(N)] ___ i __ r..(N)]
        ___ i __ r..(N):
            ___ j __ r..(N):
                __ j - 1 >= 0 a.. G[i][j] __ 1:
                    F[i][j][0] = F[i][j-1][0] + 1
                __ i - 1 >= 0 a.. G[i][j] __ 1:
                    F[i][j][1] = F[i-1][j][1] + 1

        ___ i __ r..(N-1, -1, -1):
            ___ j __ r..(N-1, -1, -1):
                __ j + 1 < N a.. G[i][j] __ 1:
                    F[i][j][2] = F[i][j+1][2] + 1
                __ i + 1 < N a.. G[i][j] __ 1:
                    F[i][j][3] = F[i+1][j][3] + 1

        ret = 0
        ___ i __ r..(N):
            ___ j __ r..(N):
                ret = max(ret, m..(F[i][j]))

        r.. ret


__ __name__ __ "__main__":
    ... Solution().orderOfLargestPlusSign(5, [[4, 2]]) __ 2
