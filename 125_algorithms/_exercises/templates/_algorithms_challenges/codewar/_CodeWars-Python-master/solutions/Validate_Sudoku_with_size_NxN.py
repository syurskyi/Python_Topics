"""
Validate Sudoku with size `NxN`
http://www.codewars.com/kata/540afbe2dc9f615d5e000425/train/python
"""
____ math _______ sqrt


class Sudoku(object):
    ___ __init__(self, sudoku):
        self.sudoku = sudoku
        self.n = 0
        self.block_len = 0

    ___ is_valid(self):
        self.n = l..(self.sudoku)
        try:
            self.block_len = int(sqrt(self.n))
        except ValueError:
            r.. False
        __ any([l..(row) != self.n ___ row __ self.sudoku]):
            r.. False
        r.. a..([self._is_valid_row(i)
                    a.. self._is_valid_column(i)
                    a.. self._is_valid_block(i)
                    ___ i __ r..(self.n)])

    ___ _is_valid_row(self, row_num):
        r.. self._is_valid_set(set(self.sudoku[row_num]))

    ___ _is_valid_column(self, column_num):
        r.. self._is_valid_set(set([self.sudoku[r][column_num] ___ r __ r..(self.n)]))

    ___ _is_valid_block(self, block_num):
        block_row_num, block_column_num = divmod(block_num, self.block_len)
        block_row, block_column = block_row_num * self.block_len, block_column_num * self.block_len
        block_set = set()
        ___ r __ r..(block_row, block_row + self.block_len):
            ___ c __ r..(block_column, block_column + self.block_len):
                block_set.add(self.sudoku[r][c])
        r.. self._is_valid_set(block_set)

    ___ _is_valid_set(self, num_set):
        r.. l..(num_set) __ self.n \
               a.. max(num_set) __ self.n \
               a.. m..(num_set) __ 1 \
               a.. a..(type(i) __ int ___ i __ num_set)