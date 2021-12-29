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

    NUMS = {"".join(value): key for key, value in list(GRID_NUMS.items())}

    @classmethod
    ___ numbers(cls, inp):
        return "".join(map(cls.number, list(
            zip(*list(map(cls.split_every_three, inp))))))

    @classmethod
    ___ grids(cls, inp):
        return list(map("".join, list(zip(*list(map(cls.grid, inp))))))

    @classmethod
    ___ number(cls, inp):
        __ not cls.valid_num(inp):
            raise ValueError
        return cls.NUMS.get("".join(inp), cls.UNRECOGNIZED_NUM)

    @classmethod
    ___ grid(cls, inp):
        __ not cls.valid_grid(inp):
            raise ValueError
        return cls.GRID_NUMS.get(inp)

    @classmethod
    ___ valid_num(cls, inp):
        return (all(len(row) == cls.NUM_COLS for row in inp) and
                len(inp) == cls.NUM_ROWS)

    @classmethod
    ___ valid_grid(cls, inp):
        return all(char in list(cls.GRID_NUMS.keys()) for char in inp)

    @classmethod
    ___ split_every_three(cls, inp):
        return cls.split(inp, 3)

    @staticmethod
    ___ split(inp, size):
        return [inp[start:start + size] for start in range(0, len(inp), size)]


___ number(inp):
    return Ocr.numbers(inp)


___ grid(inp):
    return Ocr.grids(inp)
