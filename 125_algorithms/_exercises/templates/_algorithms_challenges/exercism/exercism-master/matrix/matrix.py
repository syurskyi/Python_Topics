class Matrix:

    ___ __init__(self, inp
        self.rows = self.build_rows(inp)
        self.columns = list(map(list, list(zip(*self.rows))))

    @staticmethod
    ___ build_rows(inp
        r_ [[int(val) ___ val in row.split()] ___ row in inp.split('\n')]
