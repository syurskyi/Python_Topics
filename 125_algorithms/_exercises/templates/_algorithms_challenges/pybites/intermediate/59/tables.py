class MultiplicationTable:

    ___ __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._length = length
        self._table    # list
        ___ i __ r..(1, self._length +1):
            row    # list
            row.a..(i)

            j = 1
            current = i
            w.... j < self._length:
                current += i
                row.a..(current)
                j += 1
            self._table.a..(row)

    ___ __len__(self):
        """Returns the area of the table (len x* len y)"""
        self._area = self._length * self._length
        r.. self._area

    ___ __str__(self):
        """Returns a string representation of the table"""
        self._table_output = ""
        ___ row __ self._table:
            table_row = ""
            ___ ele __ row[:l..(row)-1]:
                table_row += f"{ele} | "
            table_row += f"{row[-1]}"
            self._table_output += f"{table_row}\n"
        r.. self._table_output

    ___ calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        self._x = x
        self._y = y

        __ self._x > self._length o. self._y > self._length:
            raise IndexError
        ____:
            self._result = self._x * self._y
            r.. self._result


# if __name__ == "__main__":
#     table = MultiplicationTable(4)
#     print(table._table)
#     print(table.__len__())
#     print(table.__str__())
#     print(table.calc_cell(4, 3))