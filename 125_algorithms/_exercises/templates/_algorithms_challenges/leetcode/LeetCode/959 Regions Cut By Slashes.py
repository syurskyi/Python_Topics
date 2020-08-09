#!/usr/bin/python3
"""
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \,
or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.


Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/,
and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\,
and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:



Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
"""
from typing ______ List


class DisjointSet:
    ___ __init__(self
        """
        unbalanced DisjointSet
        """
        self.pi = {}

    ___ union(self, x, y
        pi_x = self.find(x)
        pi_y = self.find(y)
        self.pi[pi_y] = pi_x

    ___ find(self, x
        # LHS self.pi[x]
        __ x not in self.pi:
            self.pi[x] = x
        __ self.pi[x] != x:
            self.pi[x] = self.find(self.pi[x])
        r_ self.pi[x]

class Solution:
    ___ regionsBySlashes(self, grid: List[str]) -> int:
        """
        in 1 x 1 cell
        3 possibilities
         ___
        |   |
        |___|
         ___
        |  /|
        |/__|
         ___
        |\  |
        |__\|

        4 regions in the
         ___
        |\ /|
        |/_\|
        """
        m, n = le.(grid), le.(grid[0])
        ds = DisjointSet()
        T, R, B, L = range(4)  # top, right, bottom, left
        ___ i in range(m
            ___ j in range(n
                e = grid[i][j]
                __ e __ "/" or e __ " ":
                    ds.union((i, j, B), (i, j, R))
                    ds.union((i, j, T), (i, j, L))
                __ e __ "\\" or e __ " ":  # not elif
                    ds.union((i, j, T), (i, j, R))
                    ds.union((i, j, B), (i, j, L))
                # nbr
                __ i - 1 >= 0:
                    ds.union((i, j, T), (i-1, j, B))
                __ j - 1 >= 0:
                    ds.union((i, j, L), (i, j-1, R))

                # unnessary, half closed half open
                # if i + 1 < m:
                #     ds.union((i, j, B), (i+1, j, T))
                # if j + 1 < n:
                #     ds.union((i, j, R), (i, j+1, L))


        r_ le.(set(
            ds.find(x)
            ___ x in ds.pi.keys()
        ))


__ __name__ __ "__main__":
    assert Solution().regionsBySlashes([
          " /",
          "/ "
        ]) __ 2
    assert Solution().regionsBySlashes([
          "//",
          "/ "
        ]) __ 3
