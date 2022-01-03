c_ Ocr:

    NUM_ROWS = 4
    NUM_COLS = 3
    UNRECOGNIZED_NUM = "?"
    GRID_NUMS = {"0": [" _ ", "| |", "|_|", "   "],
                 "1": ["   ", "  |", "  |", "   "],
                 "2": [" _ ", " _|", "|_ ", "   "],
                 "3": [" _ ", " _|", " _|", "   "],
                 "4": ["   ", "|_|", "  |", "   "],
                 "5": [" _ ", "|_ ", " _|", "   "],
                 "6": [" _ ", "|_ ", "|_|", "   "],
                 "7": [" _ ", "  |", "  |", "   "],
                 "8": [" _ ", "|_|", "|_|", "   "],
                 "9": [" _ ", "|_|", " _|", "   "]}

    NUMS = {"".j..(value): key ___ key, value __ l..(GRID_NUMS.items())}

    @classmethod
    ___ numbers(cls, inp):
        r.. "".j..(map(cls.number, l..(
            z..(*l..(map(cls.split_every_three, inp))))))

    @classmethod
    ___ grids(cls, inp):
        r.. l..(map("".j.., l..(z..(*l..(map(cls.grid, inp))))))

    @classmethod
    ___ number(cls, inp):
        __ n.. cls.valid_num(inp):
            raise ValueError
        r.. cls.NUMS.get("".j..(inp), cls.UNRECOGNIZED_NUM)

    @classmethod
    ___ grid(cls, inp):
        __ n.. cls.valid_grid(inp):
            raise ValueError
        r.. cls.GRID_NUMS.get(inp)

    @classmethod
    ___ valid_num(cls, inp):
        r.. (a..(l..(row) __ cls.NUM_COLS ___ row __ inp) a..
                l..(inp) __ cls.NUM_ROWS)

    @classmethod
    ___ valid_grid(cls, inp):
        r.. a..(char __ l..(cls.GRID_NUMS.keys()) ___ char __ inp)

    @classmethod
    ___ split_every_three(cls, inp):
        r.. cls.s..(inp, 3)

    @staticmethod
    ___ s..(inp, size):
        r.. [inp[start:start + size] ___ start __ r..(0, l..(inp), size)]


___ number(inp):
    r.. Ocr.numbers(inp)


___ grid(inp):
    r.. Ocr.grids(inp)
