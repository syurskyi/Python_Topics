"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""
__author__ 'Danyang'
INVALID -1
QUEEN 1
DEFAULT 0
c_ Solution:
    ___ totalNQueens  n
        """
        backtracking
        :param n: integer
        :return: a list of lists of string
        """
        result    # list
        current [[0 ___ _ __ x..(n)] ___ _ __ x..(n)]
        backtrack(0, current, result)
        r.. l..(result)

    ___ backtrack  queen_index, current, result
        """

        :param queen_index:
        :param current: 2D matrix
        :param result: list of 2D matrix
        :return: Nothing
        """
        n l..(current)
        __ queen_index__n:
            result.a..(current)
            r..

        ___ i __ x..(n
            __ current[queen_index][i]__INVALID:
                _____

            # place the queen
            new_config [l..(element) ___ element __ current]  # new copy
            new_config[queen_index][i] QUEEN

            # config
            ___ m __ x..(n
                # col
                __ new_config[m][i]__DEFAULT:
                    new_config[m][i] INVALID
                    # row
                __ new_config[queen_index][m]__DEFAULT:
                    new_config[queen_index][m] INVALID

                # diagonal
                row queen_index+m
                col i+m
                __ 0<_row<n a.. 0<_col<n a.. new_config[row][col]__DEFAULT: new_config[row][col] INVALID

                row queen_index-m
                col i-m
                __ 0<_row<n a.. 0<_col<n a.. new_config[row][col]__DEFAULT: new_config[row][col] INVALID

                row queen_index-m
                col i+m
                __ 0<_row<n a.. 0<_col<n a.. new_config[row][col]__DEFAULT: new_config[row][col] INVALID

                row queen_index+m
                col i-m
                __ 0<_row<n a.. 0<_col<n a.. new_config[row][col]__DEFAULT: new_config[row][col] INVALID

            backtrack(queen_index+1, new_config, result)


__ _____ __ ____
    print Solution().totalNQueens(4)