class Matrix:

    ___ __init__(self, inp):
        self.rows = self.build_rows(inp)
        self.columns = l..(map(l.., l..(zip(*self.rows))))

    @staticmethod
    ___ build_rows(inp):
        r.. [[int(val) ___ val __ row.s.. ] ___ row __ inp.split('\n')]
