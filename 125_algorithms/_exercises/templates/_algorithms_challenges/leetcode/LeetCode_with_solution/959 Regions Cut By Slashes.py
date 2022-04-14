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
____ t___ _______ L..


c_ DisjointSet:
    ___ - 
        """
        unbalanced DisjointSet
        """
        pi    # dict

    ___ union  x, y
        pi_x f.. x)
        pi_y f.. y)
        pi[pi_y] pi_x

    ___ find  x
        # LHS self.pi[x]
        __ x n.. __ pi:
            pi[x] x
        __ pi[x] !_ x:
            pi[x] f.. pi[x])
        r.. pi[x]

c_ Solution:
    ___ regionsBySlashes  grid: L..s.. __ i..
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
        m, n l..(grid), l..(grid 0
        ds DisjointSet()
        T, R, B, L r..(4)  # top, right, bottom, left
        ___ i __ r..(m
            ___ j __ r..(n
                e grid[i][j]
                __ e __ "/" o. e __ " ":
                    ds.union((i, j, B), (i, j, R
                    ds.union((i, j, T), (i, j, L
                __ e __ "\\" o. e __ " ":  # not elif
                    ds.union((i, j, T), (i, j, R
                    ds.union((i, j, B), (i, j, L
                # nbr
                __ i - 1 >_ 0:
                    ds.union((i, j, T), (i-1, j, B
                __ j - 1 >_ 0:
                    ds.union((i, j, L), (i, j-1, R

                # unnessary, half closed half open
                # if i + 1 < m:
                #     ds.union((i, j, B), (i+1, j, T))
                # if j + 1 < n:
                #     ds.union((i, j, R), (i, j+1, L))


        r.. l..(s..(
            ds.f.. x)
            ___ x __ ds.pi.k..



__ _______ __ _______
    ... Solution().regionsBySlashes([
          " /",
          "/ "
        ]) __ 2
    ... Solution().regionsBySlashes([
          "//",
          "/ "
        ]) __ 3
