c_ Solution:
    # @return an integer
    ___ totalNQueens  n
        res 0
        n n
        columns [-1 ___ i __ r..(n)]
        solve(columns, 0)
        r.. res

    ___ is_valid  columns, row, col
        ___ r __ r..(row
            c columns[r]
            __ c __ col:
                r.. F..
            __ a..(c - col) __ row - r:
                r.. F..
        r.. T..

    ___ solve  columns, row
        __ row __ n:
            res += 1
        ____
            ___ col __ r..(n
                __ is_valid(columns, row, col
                    columns[row] col
                    solve(columns, row + 1)
