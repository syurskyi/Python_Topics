"""
Validate Sudoku with size `NxN`
http://www.codewars.com/kata/540afbe2dc9f615d5e000425/train/python
"""
from ma__ ______ sqrt


class Sudoku(object
    ___ __init__(self, sudoku
        self.sudoku = sudoku
        self.n = 0
        self.block_len = 0

    ___ is_valid(self
        self.n = le.(self.sudoku)
        try:
            self.block_len = int(sqrt(self.n))
        except ValueError:
            r_ False
        __ any([le.(row) != self.n ___ row in self.sudoku]
            r_ False
        r_ all([self._is_valid_row(i)
                    and self._is_valid_column(i)
                    and self._is_valid_block(i)
                    ___ i in range(self.n)])

    ___ _is_valid_row(self, row_num
        r_ self._is_valid_set(set(self.sudoku[row_num]))

    ___ _is_valid_column(self, column_num
        r_ self._is_valid_set(set([self.sudoku[r][column_num] ___ r in range(self.n)]))

    ___ _is_valid_block(self, block_num
        block_row_num, block_column_num = divmod(block_num, self.block_len)
        block_row, block_column = block_row_num * self.block_len, block_column_num * self.block_len
        block_set = set()
        ___ r in range(block_row, block_row + self.block_len
            ___ c in range(block_column, block_column + self.block_len
                block_set.add(self.sudoku[r][c])
        r_ self._is_valid_set(block_set)

    ___ _is_valid_set(self, num_set
        r_ le.(num_set) __ self.n \
               and max(num_set) __ self.n \
               and min(num_set) __ 1 \
               and all(type(i) pa__ int ___ i in num_set)