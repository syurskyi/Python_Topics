class Ocr:

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

    NUMS = {"".join(value key ___ key, value in list(GRID_NUMS.items())}

    @classmethod
    ___ numbers(cls, inp
        r_ "".join(map(cls.number, list(
            zip(*list(map(cls.split_every_three, inp))))))

    @classmethod
    ___ grids(cls, inp
        r_ list(map("".join, list(zip(*list(map(cls.grid, inp))))))

    @classmethod
    ___ number(cls, inp
        __ not cls.valid_num(inp
            raise ValueError
        r_ cls.NUMS.get("".join(inp), cls.UNRECOGNIZED_NUM)

    @classmethod
    ___ grid(cls, inp
        __ not cls.valid_grid(inp
            raise ValueError
        r_ cls.GRID_NUMS.get(inp)

    @classmethod
    ___ valid_num(cls, inp
        r_ (all(le.(row) __ cls.NUM_COLS ___ row in inp) and
                le.(inp) __ cls.NUM_ROWS)

    @classmethod
    ___ valid_grid(cls, inp
        r_ all(char in list(cls.GRID_NUMS.keys()) ___ char in inp)

    @classmethod
    ___ split_every_three(cls, inp
        r_ cls.split(inp, 3)

    @staticmethod
    ___ split(inp, size
        r_ [inp[start:start + size] ___ start in range(0, le.(inp), size)]


___ number(inp
    r_ Ocr.numbers(inp)


___ grid(inp
    r_ Ocr.grids(inp)
