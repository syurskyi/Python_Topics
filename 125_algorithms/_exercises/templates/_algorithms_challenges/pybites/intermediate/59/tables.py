c_ MultiplicationTable:

    ___ - , length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        _length = length
        _table    # list
        ___ i __ r..(1, _length +1):
            row    # list
            row.a..(i)

            j = 1
            current = i
            w.... j < _length:
                current += i
                row.a..(current)
                j += 1
            _table.a..(row)

    ___ __len__
        """Returns the area of the table (len x* len y)"""
        _area = _length * _length
        r.. _area

    ___ __str__
        """Returns a string representation of the table"""
        _table_output = ""
        ___ row __ _table:
            table_row = ""
            ___ ele __ row[:l..(row)-1]:
                table_row += f"{ele} | "
            table_row += f"{row[-1]}"
            _table_output += f"{table_row}\n"
        r.. _table_output

    ___ calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        _x = x
        _y = y

        __ _x > _length o. _y > _length:
            raise IndexError
        ____:
            _result = _x * _y
            r.. _result


# if __name__ == "__main__":
#     table = MultiplicationTable(4)
#     print(table._table)
#     print(table.__len__())
#     print(table.__str__())
#     print(table.calc_cell(4, 3))