"""
Validate Sudoku with size `NxN`
http://www.codewars.com/kata/540afbe2dc9f615d5e000425/train/python
"""
____ math _______ sqrt


c_ Sudoku(o..):
    ___ - , sudoku):
        sudoku = sudoku
        n = 0
        block_len = 0

    ___ is_valid
        n = l..(sudoku)
        ___
            block_len = i..(sqrt(n))
        ______ V..
            r.. F..
        __ any([l..(row) != n ___ row __ sudoku]):
            r.. F..
        r.. a..([_is_valid_row(i)
                    a.. _is_valid_column(i)
                    a.. _is_valid_block(i)
                    ___ i __ r..(n)])

    ___ _is_valid_row  row_num):
        r.. _is_valid_set(set(sudoku[row_num]))

    ___ _is_valid_column  column_num):
        r.. _is_valid_set(set([sudoku[r][column_num] ___ r __ r..(n)]))

    ___ _is_valid_block  block_num):
        block_row_num, block_column_num = divmod(block_num, block_len)
        block_row, block_column = block_row_num * block_len, block_column_num * block_len
        block_set = set()
        ___ r __ r..(block_row, block_row + block_len):
            ___ c __ r..(block_column, block_column + block_len):
                block_set.add(sudoku[r][c])
        r.. _is_valid_set(block_set)

    ___ _is_valid_set  num_set):
        r.. l..(num_set) __ n \
               a.. m..(num_set) __ n \
               a.. m..(num_set) __ 1 \
               a.. a..(t..(i) __ i.. ___ i __ num_set)