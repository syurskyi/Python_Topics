class MultiplicationTable:

    ___ __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._length = length
        self._table = []
        for i in range(1, self._length +1):
            row = []
            row.append(i)

            j = 1
            current = i
            while j < self._length:
                current += i
                row.append(current)
                j += 1
            self._table.append(row)

    ___ __len__(self):
        """Returns the area of the table (len x* len y)"""
        self._area = self._length * self._length
        return self._area

    ___ __str__(self):
        """Returns a string representation of the table"""
        self._table_output = ""
        for row in self._table:
            table_row = ""
            for ele in row[:len(row)-1]:
                table_row += f"{ele} | "
            table_row += f"{row[-1]}"
            self._table_output += f"{table_row}\n"
        return self._table_output

    ___ calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        self._x = x
        self._y = y

        __ self._x > self._length or self._y > self._length:
            raise IndexError
        else:
            self._result = self._x * self._y
            return self._result


# if __name__ == "__main__":
#     table = MultiplicationTable(4)
#     print(table._table)
#     print(table.__len__())
#     print(table.__str__())
#     print(table.calc_cell(4, 3))